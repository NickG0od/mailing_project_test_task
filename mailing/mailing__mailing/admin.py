from django.contrib import admin
from .models import Mailing


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ["id", "start_date", "msg_text", "properties_filter", "end_date"]

