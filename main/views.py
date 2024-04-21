from django.shortcuts import render
from django.http import HttpResponse
from .models import Track, LiteratureLinks, Question, Choice
from django.shortcuts import redirect
from django.urls import reverse

def fill_question_list(type_questions):
    questions_list = []
    for question in type_questions:
            choices = Choice.objects.filter(question=question)
            question_dict = {question: choices}
            questions_list.append(question_dict)
    return questions_list


def count_percent(request, type):
    data = request.session.get(f'{type}_options')
    return int(sum(data)/len(data) * 100)

def remember_to_session(type, request):
    res = []
    for id in Question.objects.filter(type=type).values_list('id', flat=True):
        res.append(Choice.objects.filter(id=request.POST.get(f'{type}question{id}')).first().is_correct)
    request.session[f'{type}_options'] = res

def index(request):
    return render(request, 'index.html', {})

def testpage(request):
    if request.method == 'POST':
       

        remember_to_session('please', request)
        remember_to_session('refuse', request)
        remember_to_session('conflict', request)
        remember_to_session('opinion', request)
        remember_to_session('praise', request)
        remember_to_session('critisize', request)


        return redirect('result')  
    else:
        please_questions = Question.objects.filter(type='please')
        please_questions_list = fill_question_list(please_questions)
        
        refuse_questions = Question.objects.filter(type='refuse')
        refuse_questions_list = fill_question_list(refuse_questions)

        conflict_questions = Question.objects.filter(type='conflict')
        conflict_questions_list = fill_question_list(conflict_questions)

        opinion_questions = Question.objects.filter(type='opinion')
        opinion_questions_list = fill_question_list(opinion_questions)


        praise_questions = Question.objects.filter(type='praise')
        praise_questions_list = fill_question_list(praise_questions)

        critisize_questions = Question.objects.filter(type='critisize')
        critisize_questions_list = fill_question_list(critisize_questions)

        all_questions = {}
        if please_questions_list:
            all_questions['Просить'] = please_questions_list
        if refuse_questions_list:
            all_questions['Отказывать'] = refuse_questions_list
        if conflict_questions_list:
            all_questions['Конфликтовать'] = conflict_questions_list
        if opinion_questions_list:
                all_questions['Выражать мнение'] = opinion_questions_list
        if praise_questions_list:
            all_questions['Хвалить'] = praise_questions_list
        if critisize_questions_list:
                all_questions['Критиковать'] = critisize_questions_list
        
        return render(request, 'testpage.html', {'all_questions': all_questions})


def advices(request):
    return render(request, 'advices.html', {})

def materials(request):
    links = LiteratureLinks.objects.all()
    return render(request, 'materials.html', {'links': links})

def result(request):
    please_percent = count_percent(request, 'please')
    refuse_percent = count_percent(request, 'refuse')
    conflict_percent = count_percent(request, 'conflict')
    opinion_percent = count_percent(request, 'opinion')
    praise_percent = count_percent(request, 'praise')
    critisize_percent = count_percent(request, 'critisize')
    data = request.session.get('opinion_options')
    return render(request, 'result.html', {'please_percent': please_percent,'refuse_percent':refuse_percent, 'conflict_percent': conflict_percent ,'opinion_percent': opinion_percent,'praise_percent':praise_percent ,'critisize_percent':critisize_percent, 'data': data})



