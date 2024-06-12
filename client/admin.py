from django.contrib import admin
from client.models import Client


@admin.register(Client)
class PostAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'post', 'region', 'sales_channel', 'time_request')
    list_filter = ('time_request',)
    search_fields = ('region', 'sales_channel',)

