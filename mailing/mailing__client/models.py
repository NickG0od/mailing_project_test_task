from django.db import models
from django.core.validators import RegexValidator
from taggit.managers import TaggableManager
import pytz


class Client(models.Model):
    phone_regex = RegexValidator(
        regex=r'^[7]\d{10,10}$',
        message="Phone number must be entered in the format: '7XXXXXXXXXX' where X: 0-9."
    )
    mobile_operator_code_regex = RegexValidator(
        regex=r'^\d{3,3}$',
        message="Operator code must be entered in the format: 'XXX' where X: 0-9."
    )
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    phone_number = models.CharField(validators=[phone_regex], max_length=11, unique=True)
    mobile_operator_code = models.CharField(validators=[mobile_operator_code_regex], max_length=3)
    tags = TaggableManager(blank=True)
    timezone = models.CharField(choices=TIMEZONES, max_length=64, default='UTC')

    def phone_as_int(self):
        val = -1
        try:
            val = int(self.phone_number)
        except:
            pass
        return val
    
    objects = models.Manager()
    class Meta:
        ordering = ["id"]
    
