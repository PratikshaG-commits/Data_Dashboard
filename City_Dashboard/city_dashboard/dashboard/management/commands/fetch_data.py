import requests
import json
from django.core.management.base import BaseCommand
from dashboard.models import CityData

class Command(BaseCommand):
    help = 'Fetch data from Leipzig and Chemnitz APIs'

    def fetch_data(self, api_url):
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            self.stdout.write(self.style.ERROR(f'Failed to fetch data from {api_url}'))
            return None

    def handle(self, *args, **kwargs):
        leipzig_api_url = "https://opendata.leipzig.de/api/3/action/package_list"
        chemnitz_api_url = "https://services6.arcgis.com/jiszdsDupTUO3fSM/arcgis/rest/services/Stadt_FL_1/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"

        leipzig_data = self.fetch_data(leipzig_api_url)
        chemnitz_data = self.fetch_data(chemnitz_api_url)
        console.log(chemnitz_data);

        # Print the API response for Chemnitz
        self.stdout.write(self.style.SUCCESS(f'Chemnitz data: {json.dumps(chemnitz_data, indent=2)}'))

        # Save Leipzig data
        if leipzig_data and 'result' in leipzig_data:
            for item in leipzig_data['result']:
                CityData.objects.update_or_create(
                    name=item,
                    defaults={'source': 'Leipzig'}
                )

        # Save Chemnitz data
        if chemnitz_data and 'features' in chemnitz_data:
            for item in chemnitz_data['features']:
                attributes = item['attributes']
                CityData.objects.update_or_create(
                    name=attributes.get('name', 'Unknown'),
                    defaults={'source': 'Chemnitz'}
                )

        self.stdout.write(self.style.SUCCESS('Successfully fetched and stored data'))
