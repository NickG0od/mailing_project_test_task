from django.contrib import admin
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["id", "phone_number", "mobile_operator_code", "tag_list"]
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')
        
    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

