from django.shortcuts import render
# from .tasks import notify_customers
import requests

def say_hello(request):
    # notify_customers.delay('Hello')
    requests.get('https://httpbin.org/delay/2')
    return render(request, 'hello.html', {'name': 'Mosh'})
