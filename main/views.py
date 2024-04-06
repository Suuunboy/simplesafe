from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', {})
    # return HttpResponse("Hello, world. You're at the polls index.")

def testpage(request):
    return render(request, 'testpage.html', {})

def advices(request):
    return render(request, 'advices.html', {})

def materials(request):
    return render(request, 'materials.html', {})

def results(request):
    return render(request,'results.html', {})