from django.urls import path
from crops.views import get_crops_by_region_and_crop

urlpatterns = [
    path('<str:district_name>/<str:crop_name>/', get_crops_by_region_and_crop, name='crops-by-region-and-crop'),
]
