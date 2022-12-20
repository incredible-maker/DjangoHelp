from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    # return HttpResponse('my name is Jacky')
    return render(request, 'about.html')


def homepage(request):
    # return HttpResponse('welcome home')
    return render(request, 'homepage.html')


def index(request):
    return HttpResponse("Hello, world I am the king")


def lifediary(request):
    return render(request, 'lifediary.html')
