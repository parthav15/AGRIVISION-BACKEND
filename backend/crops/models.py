from django.db import models

class HistoricalData(models.Model):
    id = models.AutoField(primary_key=True)
    crop_name = models.CharField(max_length=100, verbose_name='Crop Name', default='', null=True)
    district = models.CharField(max_length=100, verbose_name='District', default='', null=True)
    year = models.PositiveIntegerField(verbose_name='Year', default=0, null=True)
    yield_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Yield Value')
    market_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Market Price')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Modified At')

    class Meta:
        verbose_name = 'Historical Data'
        verbose_name_plural = 'Historical Data'
        ordering = ['district', 'year']

    def __str__(self):
        return f"{self.crop_name} - {self.district} - {self.year}"
