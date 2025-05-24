from django.core.cache import cache
from django.shortcuts import render
from django.views.decorators.cache import cache_page
# from .tasks import notify_customers
from rest_framework.views import APIView
import requests

class HelloView(APIView):
    def get(self, request):
        response = requests.get('https://httpbin.org/delay/2')
        data = response.json()
    
        return render(request, 'hello.html', {'name': 'Eli'})

# @cache_page(5 * 60)
# def say_hello(request):
#     # notify_customers.delay('Hello')
#     response = requests.get('https://httpbin.org/delay/2')
#     data = response.json()
    
#     return render(request, 'hello.html', {'name': 'data'})
