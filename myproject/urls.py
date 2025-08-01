from django.contrib import admin
from django.urls import path, include #'include' is used to load url patterns from other apps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myApp.urls')), #connect to the urls of myApp
]
# This file defines the URL routing for the Django project.