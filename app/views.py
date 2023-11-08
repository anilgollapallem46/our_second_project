from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def walk(request):
    return HttpResponse('<h1><marquee>Tomorrow"s Plan For Walking is OLD HALL Airport</h1></marquee>')
