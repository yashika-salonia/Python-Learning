# from django.shortcuts import render
from django.http import HttpResponse 
# used to return plain text as http response
from django.shortcuts import render

# views.py headles logic for web request
def hello(request):
    return HttpResponse("Hello from django!")

def home(request):
    return render(request, 'home.html')  # Render a template named 'home.html'