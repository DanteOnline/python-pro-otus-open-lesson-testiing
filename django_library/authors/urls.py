from django.urls import path
from . import views

app_name = 'authors'  # pylint: disable=invalid-name

urlpatterns = [
    path('', views.AuthorListView.as_view(), name='authors')
]
