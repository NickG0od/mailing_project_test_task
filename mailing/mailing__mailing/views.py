from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, permissions
from datetime import datetime
import pytz
from .models import Mailing
from .serializers import MailingSerializer
from scheduler import scheduler


class MailingApiView(GenericAPIView):
    queryset = Mailing.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MailingSerializer

    def check_new_mailing(self, data):
        date_format = "%Y-%m-%dT%H:%M:%S%z"
        instance_id = data['id']
        start_date = datetime.strptime(data['start_date'], date_format)
        end_date = datetime.strptime(data['end_date'], date_format)
        current_date_utc = datetime.now(pytz.utc)
        if current_date_utc < end_date:
            run_date = None
            if current_date_utc < start_date:
                run_date = start_date.strftime("%Y-%m-%d %H:%M:%S")
            scheduler.Scheduler(instance_id=instance_id, run_date=run_date, task_id="task_1")

    def get(self, request, *args, **kwargs):
        mailings = Mailing.objects.all()
        serializer = MailingSerializer(mailings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            'start_date': request.data.get('start_date'), 
            'msg_text': request.data.get('msg_text'), 
            'properties_filter': request.data.get('properties_filter'), 
            'end_date': request.data.get('end_date')
        }
        serializer = MailingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            self.check_new_mailing(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MailingDetailApiView(GenericAPIView):
    queryset = Mailing.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MailingSerializer

    def get_object(self, mailing_id):
        try:
            return Mailing.objects.get(id=mailing_id)
        except Mailing.DoesNotExist:
            return None

    def get(self, request, mailing_id, *args, **kwargs):
        mailing_instance = self.get_object(mailing_id)
        if not mailing_instance:
            return Response(
                {"res": "Object with mailing id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = MailingSerializer(mailing_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, mailing_id, *args, **kwargs):
        mailing_instance = self.get_object(mailing_id)
        if not mailing_instance:
            return Response(
                {"res": "Object with mailing id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {}
        instance_fields = ['start_date', 'msg_text', 'properties_filter', 'end_date']
        for field in instance_fields:
            if request.data.get(field) is not None:
                data[field] = request.data.get(field)
        serializer = MailingSerializer(instance=mailing_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, mailing_id, *args, **kwargs):
        mailing_instance = self.get_object(mailing_id)
        if not mailing_instance:
            return Response(
                {"res": "Object with mailing id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        mailing_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

