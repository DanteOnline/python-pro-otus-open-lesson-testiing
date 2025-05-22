from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=32)
    birthday_year = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}: {self.birthday_year}'
