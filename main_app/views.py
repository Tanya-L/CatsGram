from .models import Cat

#from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
# from django.template import loader
from django.urls import reverse
from django.views import generic


from .models import Question, Choice
# from django.views.generic import ListView


# Use 3 parameters: request, template name, context => HttpResponse

def cattery_home(request):
    return redirect(to="cattery_welcome")


def cattery_cats(request):
    # Load only cats belonging to the logged in user
    #
    # hint: request.user...
    #
    template_data = {
        'cats': Cat.objects.all()
    }

    return render(request, 'cattery/cattery_cats.html', template_data)


def cattery_welcome(request):
    return render(request, 'cattery/cattery_welcome.html')


def cattery_photo(request):
    return render(request, 'cattery/cattery_photo.html')


# new def   now
def cattery_cat(request, cat_id):

    template_data = {
        'cats': Cat.objects.all(),
        'cat': Cat.objects.get(pk=long(cat_id))
    }

    return render(request, 'cattery/cattery_cat.html', template_data)



#def all_cats(request):
#    # all_cats = cats.object.filter(ispublic=True)
#    return render(request, 'all_cats.html', {'cats': cats})

# class AllCatsView(ListView):
#     model = Cat
#     template_name = "cat/all_cats.html"
#     context_object_name = "cats"





# part 4 tutorial
class IndexView(generic.ListView):
    template_name = "polls_index.html"
    context_object_name = "latest_question_list"

#return the last five published questions.
    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "cattery_polls_detail.html"


class ResultView(generic.DetailView):
    model = Question
    template_name = "cattery_polls_result.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #     Redisplay thee question voting form.
        return render(request, "cattery_polls_detail.html", {"question": question, "error_message": "You didn't select a choice.",})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))
