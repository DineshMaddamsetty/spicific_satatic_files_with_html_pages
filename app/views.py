from django.shortcuts import render


def navbar(request):
    return render(request,'navbar.html')

def header(request):
    return render(request,'header.html')

def bio(request):
    return render(request,'bio.html')
# Create your views here.
