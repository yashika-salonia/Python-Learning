from django.urls import path
from .views import is_palindrome

urlpatterns = [
    path('check/', is_palindrome, name='is_palindrome'),
]