from django.test import TestCase, Client
from courses.models import Course
from students.models import Student
from datetime import date

# Create your tests here.

class StudentTest(TestCase):
	def test_student_pages(self):
		client = Client()
		response = client.get('/student/')
		self.assertEqual(response.status_code, 200)

		response = client.get('/student/1/')
		self.assertEqual(response.status_code, 404)

# Create your tests here.
