# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET'])
def add(request):
    a = int(request.GET.get('a', 0))
    b = int(request.GET.get('b', 0))
    return Response({'sum': a + b})