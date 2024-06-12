from rest_framework import viewsets
from news.models import News
from news.serializers import NewsSerializer


class NewsAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all().order_by('-time_created')
    serializer_class = NewsSerializer
