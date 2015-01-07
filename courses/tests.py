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

        coach_1 = Coach.objects.create(first_name='Petr',
                                       last_name='Ivanov',
                                       email="example@example.com",
                                       phone_number='050066095'
                                       )

        course1 = Course.objects.create(name='PyBursa02',
                                        start_date=date(2015, 2, 16),
                                        end_date=date(2015, 4, 16),
                                        description='new course',
                                        coach='coach',
                                        assistant='assistant',
                                        technology='p')
		