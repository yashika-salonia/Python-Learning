from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('', include('helloapp.urls')),
    path('', include('addvar.urls')),
    path('', include('palindrome_checker.urls')),
    path('', include('to_do_project.urls')),
]
