from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse


class AccountTests(TestCase):
    def test_register_creates_user_and_profile(self):
        response = self.client.post(reverse('register'), {
            'username': 'localtester', 'email': 'tester@example.com',
            'password1': 'Local-Test-57924!', 'password2': 'Local-Test-57924!',
        })
        self.assertRedirects(response, reverse('login'))
        user = User.objects.get(username='localtester')
        self.assertEqual(user.profile.user_id, user.pk)
        self.assertTrue(user.check_password('Local-Test-57924!'))

    def test_profile_requires_login(self):
        response = self.client.get(reverse('profile'))
        self.assertRedirects(response, reverse('login') + '?next=/users/profile/')

    def test_login_and_profile_update(self):
        user = User.objects.create_user('tester', password='Local-Test-57924!')
        response = self.client.post(reverse('login'), {
            'username': user.username, 'password': 'Local-Test-57924!',
        })
        self.assertRedirects(response, reverse('home'))
        self.assertEqual(self.client.get(reverse('profile')).status_code, 200)
        response = self.client.post(reverse('profile'), {
            'username': 'tester', 'email': 'tester@example.com',
            'full_name': 'Local Tester', 'bio': 'Development profile',
        })
        self.assertRedirects(response, reverse('profile'))
        user.refresh_from_db()
        self.assertEqual(user.profile.full_name, 'Local Tester')

    def test_logout_form_uses_post_and_csrf(self):
        user = User.objects.create_user('tester')
        client = Client(enforce_csrf_checks=True)
        client.force_login(user)
        response = client.get(reverse('home'))
        self.assertContains(response, 'method="post" action="/users/logout/"')
        self.assertEqual(client.post(reverse('logout')).status_code, 403)
        response = client.post(reverse('logout'), {
            'csrfmiddlewaretoken': client.cookies['csrftoken'].value,
        })
        self.assertRedirects(response, reverse('login'))
        self.assertNotIn('_auth_user_id', client.session)
