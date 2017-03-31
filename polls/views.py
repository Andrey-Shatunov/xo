from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404,render
from django.http import Http404
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    print(context)
    return render(request, 'polls/my.html', context)

