from django.db import models
from django.utils.timezone import now, timedelta


class Mailing(models.Model):
    def properties_filter_default():
        return [{'operator_code': None}, {'tag': None}]

    start_date = models.DateTimeField(default=now, null=False, blank=False)
    msg_text = models.CharField(max_length=255, null=True, blank=True)
    properties_filter = models.JSONField(default=properties_filter_default, null=True, blank=True)
    end_date = models.DateTimeField(default=now()+timedelta(1), null=False, blank=False)

    objects = models.Manager()
    class Meta:
        ordering = ["id"]

