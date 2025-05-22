from django.urls import reverse
from django.test import TestCase
from mixer.backend.django import mixer
from authors.models import Author


class AuthorListViewTestCase(TestCase):

    def setUp(self):
        mixer.cycle(5).blend(Author)

    def test_get(self):
        url = reverse('authors:authors')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
