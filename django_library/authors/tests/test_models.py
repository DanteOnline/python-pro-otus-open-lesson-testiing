import os
import json
import factory
from django.test import TestCase
from django.conf import settings
from mixer.backend.django import mixer
from authors.models import Author


class AuthorTestCase(TestCase):

    def setUp(self):
        filepath = os.path.join(settings.BASE_DIR, 'authors', 'tests', 'data', 'author.json')
        with open(filepath) as f:
            author_data = json.load(f)
            self.name = author_data['name']
            self.birthday_year = author_data['birthday_year']

    def test_str_native(self):
        # django native
        author = Author.objects.create(name=self.name, birthday_year=self.birthday_year)
        self.assertEqual(f'{self.name}: {self.birthday_year}', str(author))

    def test_str_mixer(self):
        # mixer
        author = mixer.blend(Author, name=self.name, birthday_year=self.birthday_year)
        self.assertEqual(f'{self.name}: {self.birthday_year}', str(author))

    def test_str_factory_boy(self):
        # factory boy
        class AuthorFactory(factory.django.DjangoModelFactory):
            class Meta:
                model = 'authors.Author'

        author = AuthorFactory(name=self.name, birthday_year=self.birthday_year)
        self.assertEqual(f'{self.name}: {self.birthday_year}', str(author))
