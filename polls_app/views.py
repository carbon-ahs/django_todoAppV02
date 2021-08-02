from django.http.response import Http404
from polls_app.models import Question
from django.shortcuts import get_object_or_404, render, redirect

'''
from .models import 
from .forms import 
'''
def home(request):

    try:
        all_questions = Question.objects.all()
    except Exception as e:
        raise Http404('No Qus Here!!')

    contex = {
        'key': 'value',
        'all_questions': all_questions,
    }
    return render(request, 'home.html', contex)



def about(request):
    contex = {
        'key': 'value',
    }
    return render(request, 'about.html', contex)

def detail(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    
    
    contex = {
        'key': 'value',
        'question': question,
    }
    return render(request, 'detail.html', contex)


def result(request, question_id):
    contex = {
        'key': 'value',
    }
    return render(request, 'result.html', contex)


def vote(request, question_id):
    contex = {
        'key': 'value',
    }
    return render(request, 'vote.html', contex)