from django.http import JsonResponse
from crops.models import HistoricalData

def get_crops_by_region_and_crop(request, district_name, crop_name):
    data = HistoricalData.objects.filter(district=district_name, crop_name=crop_name).values()
    return JsonResponse(list(data), safe=False)
