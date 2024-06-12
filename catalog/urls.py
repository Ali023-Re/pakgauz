from django.urls import path

from catalog.views import BrandAPIList, BrandAPIDetail, ProductAPIDetail, СategoryAPIList, СategoryAPIDetail, BrandSubcategoryAPIList, СategorySubcategoryAPIList


urlpatterns = [
    path('brand', BrandAPIList.as_view()),
    path('brand/<brand_id>/', BrandAPIDetail.as_view()),
    path('brand/<brand_id>/<int:pk>', ProductAPIDetail.as_view()),
    path('brand/<brand_id>/subcategory', BrandSubcategoryAPIList.as_view()),
    path('category', СategoryAPIList.as_view()),
    path('category/<category_id>/', СategoryAPIDetail.as_view()),
    path('category/<category_id>/<int:pk>', ProductAPIDetail.as_view()),
    path('category/<category_id>/subcategory', СategorySubcategoryAPIList.as_view())
]