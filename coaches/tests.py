from django.test import TestCase, Client
from coaches.models import Coach
from datetime import date

# Create your tests here.

class CoachTest(TestCase):
	def test_coach_pages(self):
		client = Client()
		response = client.get('/coach/')
		self.assertEqual(response.status_code, 200)

		response = client.get('/coach/1/')
		self.assertEqual(response.status_code, 404)

# Create your tests here.
