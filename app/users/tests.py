from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User


class UserTests(APITestCase):
    def setUp(self):
        self.create_user_url = reverse('user-create-user')
        self.search_user_url = reverse('user-search-user')
        self.retrieve_user_url = reverse('user-retrieve-user')

        self.user_data = {
            "last_name": "Иванов",
            "first_name": "Иван",
            "middle_name": "Иванович",
            "date_of_birth": "1990-01-01",
            "passport_number": "1234 567890",
            "place_of_birth": "Москва",
            "phone_number": "71234567890",
            "email": "ivanov@example.com",
            "registration_address": "Москва, ул. Ленина, д. 1",
            "residential_address": "Москва, ул. Ленина, д. 2"
        }

        self.client.post(self.create_user_url, self.user_data, format='json')

    def test_create_user(self):
        user_data = {
            "last_name": "Иванов",
            "first_name": "Иван",
            "middle_name": "Иванович",
            "date_of_birth": "1990-01-01",
            "passport_number": "1234 567891",
            "place_of_birth": "Москва",
            "phone_number": "71234567891",
            "email": "ivanov1@example.com",
            "registration_address": "Москва, ул. Ленина, д. 1",
            "residential_address": "Москва, ул. Ленина, д. 2"
        }
        response = self.client.post(self.create_user_url, user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_search_user(self):
        response = self.client.get(self.search_user_url, {'search': 'Иванов'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_retrieve_user(self):
        user = User.objects.get(email=self.user_data['email'])
        response = self.client.get(self.retrieve_user_url, {'id': user.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.user_data['email'])
