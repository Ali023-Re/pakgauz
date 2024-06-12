from rest_framework import routers
from news.views import NewsAPIView
from django.urls import path, include


router = routers.SimpleRouter()
router.register(r'', NewsAPIView),


urlpatterns = [
    path('', include(router.urls)),
]
