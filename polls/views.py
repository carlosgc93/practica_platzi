from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question, Choice

# Create your views here.

def index (request):
    lastest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {"lastest_question_list":lastest_question_list})


def detail(request, question_id):
    return HttpResponse(f"Estas viendo la pregunta número: {question_id}")

def result(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta número: {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Estas votando por la pregunta: {question_id}")