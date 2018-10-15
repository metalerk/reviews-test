from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status

from users.models import Reviewer
from companies.models import Company
from .models import Review


class BaseTestCase(APITestCase):
	client = APIClient(enforce_csrf_checks=True)

	def setUp(self):
		self.email = 'testuser@test.com'
		self.username = 'testuser'
		self.password = 'passwd'
		self.user = Reviewer.objects.create_user(
			self.username, self.email, self.password)

		self.data = {
			'username': self.username,
			'password': self.password
		}


	def authenticate(self):
		return self.client.post(
			'/api/user/auth/',
			self.data,
			format='json',
		)


class CompanyTestCase(BaseTestCase):
	def setUp(self):
		super(CompanyTestCase, self).setUp()

		Company.objects.create(
			name='Test Company'
		)

		Review.objects.create(
			company=Company.objects.first(),
			reviewer=Reviewer.objects.first(),
			rating=5,
			title='test review',
			summary='test text',
			is_employee=True,
			ip_address='192.168.1.1'
		)


	def test_retrieve_companies(self):
		auth = self.authenticate()
		response = self.client.get(
			'/api/company/get_companies/',
			HTTP_AUTHORIZATION='JWT ' + auth.json().get('token')
		)

		self.assertEqual(response.status_code, status.HTTP_200_OK)


	def test_create_review(self):
		auth = self.authenticate()
		body = {
				'company': Company.objects.first().id.__str__(),
				'rating': 5,
				'title': 'Rocks!',
				'summary': 'Cool',
				'is_employee': True,
			}
		response = self.client.post(
			'/api/review/post_review/',
			body,
			HTTP_AUTHORIZATION='JWT ' + auth.json().get('token')
		)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)


	def test_retrieve_reviews(self):
		auth = self.authenticate()
		response = self.client.get(
			'/api/review/get_reviews/',
			HTTP_AUTHORIZATION='JWT ' + auth.json().get('token')
		)

		self.assertEqual(response.status_code, status.HTTP_200_OK)

