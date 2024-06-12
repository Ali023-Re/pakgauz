from rest_framework import serializers
from catalog.models import Brand, Сategory, Subcategory, Product


class BrandSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Brand
        fields = ('id', 'title', 'photo', 'contain', 'category')


class СategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Сategory
        fields = ('id', 'title', 'photo', 'contain')


class SubcategorySerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Subcategory
        fields = ('id', 'title', 'category')


class ProductSerializer(serializers.ModelSerializer):
    subcategory = serializers.StringRelatedField()
    brand_name = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ('id', 'title', 'photo', 'contain', 'brand_name',  'subcategory', 'packing', 'count_in_box')
