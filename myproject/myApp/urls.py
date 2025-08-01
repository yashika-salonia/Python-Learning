# for url routing
from django.urls import path
# importing our view 
from .views import hello

urlpatterns = [
    path('', hello, name='hello'),
]