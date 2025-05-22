from django.views.generic import ListView
from .models import Author


class AuthorListView(ListView):
    model = Author
