from rest_framework import viewsets, generics
from catalog.models import Brand, Сategory, Subcategory, Product
from catalog.serializers import BrandSerializer, СategorySerializer, SubcategorySerializer, ProductSerializer


class BrandAPIList(generics.ListAPIView):
    queryset = Brand.objects.all().order_by('title')
    serializer_class = BrandSerializer


class BrandAPIDetail(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):

        queryset = Product.objects.filter(stock=True).filter(brand_name=self.kwargs['brand_id'])
        subcategory = self.request.query_params.get('subcategory')
        if subcategory:
            queryset = queryset.filter(subcategory=subcategory)
        return queryset


class СategoryAPIList(generics.ListAPIView):
    queryset = Сategory.objects.all().order_by('title')
    serializer_class = СategorySerializer


class СategoryAPIDetail(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Product.objects.filter(stock=True).filter(subcategory__category=self.kwargs['category_id']).order_by('brand_name')
        subcategory = self.request.query_params.get('subcategory')
        if subcategory:
            queryset = queryset.filter(subcategory=subcategory)
        return queryset


class СategorySubcategoryAPIList(generics.ListAPIView):
    serializer_class = SubcategorySerializer

    def get_queryset(self, *args, **kwargs):

        return Subcategory.objects.filter(category=self.kwargs['category_id']).order_by('title')


class BrandSubcategoryAPIList(generics.ListAPIView):
    serializer_class = SubcategorySerializer

    def get_queryset(self, *args, **kwargs):

        return Subcategory.objects.filter(product__brand_name=self.kwargs['brand_id']).distinct('title').order_by('title')


class ProductAPIDetail(generics.RetrieveAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

