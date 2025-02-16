import os
import csv
import random
from django.core.management.base import BaseCommand
from crops.models import HistoricalData

CROP_NAME = "Wheat"

def generate_market_price(yield_value):
    return round(yield_value * random.uniform(1.2, 1.8), 2)

class Command(BaseCommand):
    help = 'Import crop yield data from CSV'

    def handle(self, *args, **options):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(current_dir, 'CROP_YIELD_WHEAT.csv')
        
        if not os.path.exists(csv_path):
            self.stderr.write(self.style.ERROR(f"CSV file not found at {csv_path}"))
            return

        with open(csv_path, 'r', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            
            if 'District/Year' not in reader.fieldnames:
                self.stderr.write(self.style.ERROR("'District/Year' column not found in CSV header"))
                return

            for row in reader:
                district = row['District/Year'].strip()
                for year in range(2013, 2023):
                    year_str = str(year)
                    if year_str not in row:
                        continue

                    try:
                        yield_value = float(row[year_str])
                        HistoricalData.objects.create(
                            district=district,
                            year=year,
                            crop_name=CROP_NAME,
                            yield_value=yield_value,
                            market_price=generate_market_price(yield_value)
                        )
                    except ValueError as e:
                        self.stderr.write(self.style.WARNING(f"Error processing {district} {year}: {e}"))

        self.stdout.write(self.style.SUCCESS("Data imported successfully"))