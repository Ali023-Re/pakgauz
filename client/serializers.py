from rest_framework import serializers
from client.models import Client


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('id', 'full_name', 'post', 'region', 'sales_channel', 'phone', 'email', 'comment', 'time_request')