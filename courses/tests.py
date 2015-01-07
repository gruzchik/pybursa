from django.test import TestCase, Client
from courses.models import Course
from coaches.models import Coach
from datetime import date

# Create your tests here.

class CourseTest(TestCase):
    def test_course_pages(self):
        client = Client()
        response = client.get('/course/')
        self.assertEqual(response.status_code, 200)

        response = client.get('/course/1/')
        self.assertEqual(response.status_code, 404)
		