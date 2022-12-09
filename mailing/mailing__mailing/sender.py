from django.db.models import Sum, Q
import requests
from datetime import datetime
import pytz
from mailing__mailing.models import Mailing
from mailing__client.models import Client
from mailing__message.models import Message
from mailing__message.views import MessageApiView


def send_mailing(mailing_id):
    mailing_instance = Mailing.objects.filter(id=mailing_id).first()
    if not mailing_instance or mailing_instance.id is None:
        return "ERROR. Object with mailing id does not exists."
    properties_filter = mailing_instance.properties_filter
    if isinstance(properties_filter, list):
        operator_code_filter = []
        tag_filter = []
        for p_filter in properties_filter:
            if "operator_code" in p_filter and isinstance(p_filter['operator_code'], str):
                operator_code_filter.append(p_filter['operator_code'])
            if "tag" in p_filter and isinstance(p_filter['tag'], str):
                tag_filter.append(p_filter['tag'])
        if len(operator_code_filter) > 0 or len(tag_filter) > 0:
            found_clients = Client.objects.filter(Q(mobile_operator_code__in=operator_code_filter) | Q(tags__name__in=tag_filter)).distinct()
            for client in found_clients:
                try:
                    new_msg = Message(sending_status=0, mailing=mailing_instance, client=client)
                    new_msg.save()
                    send_to_external_api(new_msg.id)
                except Exception as e:
                    print(e)
                    pass
    return "ERROR. No clients found by mailing's filter."


def send_to_external_api(message_id):
    message_instance = Message.objects.filter(id=message_id).first()
    if not message_instance or message_instance.id is None:
        return "ERROR. Object with message id does not exists."
    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDIwMzE2MTcsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6Im5pYXlzaGluIn0.vvsO4pdWYCXAfeiGAgaytNJCgEDXzai4phHaIBdyhXE"
    end_date = message_instance.mailing.end_date
    current_date_utc = datetime.now(pytz.utc)
    if current_date_utc >= end_date:
        try:
            message_instance.sending_status = -1
            message_instance.save()
        except:
            pass
        return ""
    response = requests.post(f'https://probe.fbrq.cloud/v1/send/{message_instance.id}', 
        headers={'Authorization': f'Bearer {access_token}'},
        json={
            "id": message_instance.id, 
            "phone": message_instance.client.phone_as_int(), 
            "text": message_instance.mailing.msg_text
        }
    )
    if response.status_code == 200 and response.json()['code'] == 0:
        try:
            message_instance.sending_status = 1
            message_instance.save()
        except:
            pass
    else:
        MessageApiView.retry_sending(message_instance)

