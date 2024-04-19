from django.shortcuts import render
from django.http import HttpResponse
from .models import Track, LiteratureLinks
from django.shortcuts import redirect
from django.urls import reverse


def index(request):
    return render(request, 'index.html', {})
    # return HttpResponse("Hello, world. You're at the polls index.")

def testpage(request):
    if request.method == 'POST':
        selected_options = [request.POST.get(f'question{x}') for x in range(1, 5)] 
        # selected_option = request.POST.get('question1')
        request.session['selected_options'] = selected_options
        return redirect('result')  
    return render(request, 'testpage.html')


def advices(request):
    return render(request, 'advices.html', {})

def materials(request):
    links = LiteratureLinks.objects.all()
    return render(request, 'materials.html', {'links': links})

def result(request):
    selected_options = request.session.get('selected_options')
    counter = 0
    return render(request, 'result.html', {'selected_options': selected_options, 'counter': counter})

def results(request):
    return render(request,'results.html', {})


