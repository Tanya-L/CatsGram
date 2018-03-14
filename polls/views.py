# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
# from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views import generic


from .models import Question, Choice


# part 4 tutorial
class IndexView(generic.ListView):
    template_name = "polls_index.html"
    context_object_name = "latest_question_list"

    #return the last five published questions.
    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls_detail.html"


class ResultView(generic.DetailView):
    model = Question
    template_name = "polls_result.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #     Redisplay thee question voting form.
        return render(request, "polls_detail.html", {"question": question, "error_message": "You didn't select a choice.",})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))