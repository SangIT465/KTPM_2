from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class TestLoginCase(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpass123'
        User = get_user_model()
        User.objects.create_user(username=self.username, password=self.password)

    def test_login_success(self):
        # Sử dụng namespace 'accounts:login'
        response = self.client.post(reverse('accounts:login'), {
            'username': self.username,
            'password': self.password
        })
        self.assertEqual(response.status_code, 302)