from django.urls import path
from client.views import ClientAPIView

urlpatterns = [
    path('', ClientAPIView.as_view())
]