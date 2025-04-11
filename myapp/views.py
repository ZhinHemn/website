from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("Welcome to my website, my name is Zhin, from Computer Science, in University of Sulaymaniyah!")