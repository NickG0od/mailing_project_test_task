from django.db import models
from django.utils.timezone import now, timedelta
from mailing__mailing.models import Mailing
from mailing__client.models import Client


class Message(models.Model):
    SENDING_STATUS_CHOICES = [
        (1, 'Success'),
        (0, 'Pending'),
        (-1, 'Failure')
    ]

    sending_date = models.DateTimeField(default=now, null=False, blank=False)
    sending_status = models.IntegerField(choices=SENDING_STATUS_CHOICES, default=0)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    objects = models.Manager()
    class Meta:
        ordering = ["id"]

