from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

# API endpoint example that could be used by React
def api_example(request):
    data = {
        'message': 'Hello from Django API!',
        'items': ['Item 1', 'Item 2', 'Item 3']
    }
    return JsonResponse(data)
