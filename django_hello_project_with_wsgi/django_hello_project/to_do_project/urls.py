from django.urls import path
from .views import add_todo

urlpatterns = [
    path('add/', add_todo, name='add_todo'),
]