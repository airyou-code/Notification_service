from django.contrib import admin
from .models import Client, Mailing, Message

class MailingAdmin(admin.ModelAdmin):
    list_display = ["id", "start_time", "end_time", "text"]
    search_fields = ["id"]
    list_filter = ["start_time", "end_time"]


class ClientAdmin(admin.ModelAdmin):
    list_display = ["id", "phone_number", "operator", "tag"]
    search_fields = ["id"]
    list_filter = ["operator", "tag"]


class MessageAdmin(admin.ModelAdmin):
    list_display = ["id", "client", "sending_status"]
    search_fields = ["id"]
    list_filter = ["sending_status", "client"]


admin.site.register(Client, ClientAdmin)
admin.site.register(Mailing, MailingAdmin)
admin.site.register(Message, MessageAdmin)

