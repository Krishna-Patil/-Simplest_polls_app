from django.views.generic import ListView, DetailView, View, TemplateView
from django.shortcuts import get_object_or_404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .models import *
# Create your views here.


class PollsIndexView(ListView):
    model = Question
    template_name = 'polls_list.html'


class PollsDetailView(DetailView, View):
    model = Question
    template_name = 'polls_detail.html'


def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        choice_id = request.POST.get('choice')
        selected_choice = question.choice_set.get(id=choice_id)
        selected_choice.votes += 1
        selected_choice.save()
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls_detail.html', {'question': question})
    else:
        return HttpResponseRedirect(reverse('polls_list'))
