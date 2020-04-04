from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return HttpResponse("Hello Django!!")

def sign_in(request):
    return render(request, 'Login.html')

def main_page(request):
    return render(request, 'main.html')

@csrf_exempt
def info_page(request):
    if request.method == 'POST':
        print(request.body)
    return render(request, 'group_info.html')