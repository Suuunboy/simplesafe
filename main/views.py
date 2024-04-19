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


def index(request):
    return render(request, 'index.html', {})

def testpage(request):
    if request.method == 'POST':
        selected_options = [request.POST.get(f'pleasequestion{x}') for x in range(1, 5)] 
        # selected_option = request.POST.get('question1')
        request.session['selected_options'] = selected_options
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
    selected_options = request.session.get('selected_options')
    counter = 0
    return render(request, 'result.html', {'selected_options': selected_options, 'counter': counter})

def results(request):
    return render(request,'results.html', {})


