import json

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import ChatMessage


class ChatTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.alice = User.objects.create_user('alice')
        cls.bob = User.objects.create_user('bob')
        cls.carol = User.objects.create_user('carol')

    def test_endpoints_require_login(self):
        for name in ('chat_window', 'get_messages', 'get_users', 'send_message'):
            with self.subTest(endpoint=name):
                self.assertEqual(self.client.get(reverse(name)).status_code, 302)

    def test_send_and_read_conversation(self):
        self.client.force_login(self.alice)
        response = self.client.post(reverse('send_message'), json.dumps({
            'receiver_id': self.bob.pk, 'message': 'Hello 👋',
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        message = ChatMessage.objects.get(pk=response.json()['message']['id'])
        self.assertEqual(message.sender, self.alice)
        self.assertFalse(message.is_read)
        self.client.force_login(self.bob)
        users = self.client.get(reverse('get_users')).json()['users']
        self.assertTrue(next(u for u in users if u['id'] == self.alice.pk)['unread'])
        response = self.client.get(reverse('get_messages_with_user', args=[self.alice.pk]))
        self.assertEqual(response.json()['messages'][0]['message'], 'Hello 👋')
        message.refresh_from_db()
        self.assertTrue(message.is_read)

    def test_other_conversations_are_private(self):
        ChatMessage.objects.create(sender=self.bob, receiver=self.carol, message='Private')
        self.client.force_login(self.alice)
        self.assertEqual(self.client.get(reverse('get_messages')).json()['messages'], [])
        response = self.client.get(reverse('get_messages_with_user', args=[self.bob.pk]))
        self.assertEqual(response.json()['messages'], [])

    def test_empty_message_is_rejected(self):
        self.client.force_login(self.alice)
        response = self.client.post(reverse('send_message'), json.dumps({
            'receiver_id': self.bob.pk, 'message': '',
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertFalse(ChatMessage.objects.exists())

    def test_send_requires_post(self):
        self.client.force_login(self.alice)
        self.assertEqual(self.client.get(reverse('send_message')).status_code, 405)

    def test_user_list_excludes_self(self):
        self.client.force_login(self.alice)
        users = self.client.get(reverse('get_users')).json()['users']
        self.assertEqual({u['id'] for u in users}, {self.bob.pk, self.carol.pk})
