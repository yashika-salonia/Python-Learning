# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET'])
def is_palindrome(request):
    word = request.GET.get('word', '')
    return Response({'palindrome': word == word[::-1]})