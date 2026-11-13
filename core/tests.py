from django.test import TestCase
from django.urls import reverse


class CoreTests(TestCase):
    def test_home_renders_react_mount(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, '<div id="root"></div>')
        self.assertTemplateUsed(response, 'core/index.html')

    def test_example_api(self):
        response = self.client.get(reverse('api_example'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'message': 'Hello from Django API!',
            'items': ['Item 1', 'Item 2', 'Item 3'],
        })
