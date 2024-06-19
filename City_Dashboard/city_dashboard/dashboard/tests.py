from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import CityData

class CityDataTest(TestCase):
    def test_data_entry(self):
        entry = CityData.objects.create(city="Leipzig", data={"population": 600000})
        self.assertEqual(entry.city, "Leipzig")
        self.assertEqual(entry.data['population'], 600000)
