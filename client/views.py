from django.shortcuts import render
from rest_framework import generics
from client.serializers import ClientSerializer
from client.models import Client
from rest_framework.permissions import AllowAny


class ClientAPIView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [AllowAny]
