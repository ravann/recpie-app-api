from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')

TOKEN_URL = reverse('user:token')


def create_user(params):
    return get_user_model().objects.create_user(**params)


class PublicUserAPITest(TestCase):
    """Test the users public API """

    def setUp(self):
        self.client = APIClient()

    def test_valid_user_success(self):
        """Test creating user payload is successful"""
        payload = {
            "email": "user1@test.com",
            "password": "testpass",
            "name": "Test Name"
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_exists(self):
        """Test creating duplicate user"""
        payload = {
            "email": 'user1@test.com',
            "password": "testpass",
            "name": "Test Name"
        }

        create_user(payload)
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test that the password must be more than 5 characters"""
        payload = {
            "email": "user1@test.com",
            "password": "t",
            "name": "Test Name"
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()

        self.assertFalse(user_exists)

    def test_create_token_for_user(self):
        """Test that a token is created for user"""
        payload = {
            "email": "test@test.com",
            "password": "testpass",
        }
        create_user(payload)
        print("Payload is %s" % payload)
        res = self.client.post(TOKEN_URL, payload)
        print("Authenticated response is : %s" % res.data)
        self.assertIn('token', res.data)

    def test_create_token_invalid_credentials(self):
        """Test that token is not created if invalid credentials are given"""
        payload = {
            "email": "test@test.com",
            "password": "testpass"
        }
        create_user(payload)
        payload['password'] = 'newpass'
        res = self.client.post(TOKEN_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', res.data)

    def test_create_token_no_user(self):
        """Test that token is not created if user doesnt exist"""
        payload = {
            "email": "test@test.com",
            "password": "testpass"
        }
        res = self.client.post(TOKEN_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', res.data)

    def test_create_token_missing_password(self):
        """Test that token is not created if invalid credentials are given"""
        payload = {
            "email": "test@test.com",
            "password": "testpass"
        }
        create_user(payload)
        payload = {'email': 'test@test.com'}
        res = self.client.post(TOKEN_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', res.data)
