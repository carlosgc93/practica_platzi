from webbrowser import get
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import Question, Choice
from django.urls import reverse

# Create your views here.

def index (request):
    lastest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {"lastest_question_list":lastest_question_list})


def detail(request, question_id):
    question= get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question":question})


def result(request, question_id):
    question= get_object_or_404(Question, pk=question_id)
    return render (request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question= get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render (request, "polls/detail.html", {"question": question, "error_message":"No elegiste bien"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:result", args=(question_id,)))