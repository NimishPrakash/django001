from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse('Hello this is my first Django Project')
    return render(request, 'templates01/index.html')

def name(request):
    return HttpResponse('Project name - django001')

def about(request):
    return HttpResponse('Nimish Prakash')

def db(request):
    return HttpResponse('Database')



