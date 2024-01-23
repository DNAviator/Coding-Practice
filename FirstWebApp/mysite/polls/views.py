from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    template = loader.get_template("polls/question_detailed.html")
    q = Question.objects.get(id=question_id)
    context = {"id": question_id,
               "text": q.question_text,
               "time": q.pub_date}
    return HttpResponse(template.render(context, request))


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
