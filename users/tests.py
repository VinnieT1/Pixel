from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class RegistrationTestCase(TestCase):
    def test_valid_registration(self):
        response = self.client.post(reverse('register'), {'username': 'testuser', 'password1': 'testpassword', 'password2': 'testpassword'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertEqual(User.objects.filter(username='testuser').count(), 1)

    def test_invalid_registration(self):
        response = self.client.post(reverse('register'), {'username': 'testuser', 'password1': 'testpassword', 'password2': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        # 200 because it's supposed to render home instead of a redirect

class LoginTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_valid_login(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    def test_invalid_login(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        # 200 because it's supposed to render home instead of a redirect
        