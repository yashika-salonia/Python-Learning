from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('hello/', include('helloapp.urls')),
    path('add/', include('addvar.urls')),
]
