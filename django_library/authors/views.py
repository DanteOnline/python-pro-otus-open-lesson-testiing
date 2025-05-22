from django.views.generic import ListView
from .models import Author
from django.shortcuts import render


class AuthorListView(ListView):
    model = Author
