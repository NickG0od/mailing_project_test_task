from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["id", "sending_date", "sending_status", "mailing", "client"]
    list_filter = ["sending_status", "mailing", "client"]

