from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from random import randint

# Create your views here.

from blog.models import Question, Choice, Category

# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name='latest_question_list'
#
#     def get_queryset(self):
#         return Question.objects.order_by('Question.pub_date')[:5]
#
# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'
#
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'

def index(request, *params):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    category_list = Category.objects.all()
    category = request.GET.get('category', '')
    question_list = Question.objects.all()
    # print("Category is ", category)
    # # question_list =
    # print("Question_list is ", question_list)
    # for q in question_list:
    #     print("For loop is ", q.categories.all())
    if category:
        question_list = Question.objects.filter(categories__slug=category)

    context = {
        'latest_question_list': latest_question_list,
        'category_list' : category_list,
        'question_list' : question_list,
        'category' : category,

    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    related_categories = []
    for c in question.categories.all():
        related_categories.append(c)
    print("related categories is ", related_categories)
    random_related_category = related_categories[randint(0, (len(related_categories)-1))]
    print("random_related_category is ", random_related_category)
    # print(related)
    related = Question.objects.exclude(slug=question.slug)
    print("Questions excluding current is: ", related)
    related = related.filter(categories__slug=random_related_category.slug).order_by('?').first()
    # print("Questions excluding current with related category is: ", related)
    print("Random related question is: ", related)
    print(related.id)
    # related = get_object_or_404(Question, pk=related.id)
    # print(related)
    context = {
        'question': question,
        'related': related,
        }
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def category(request, category__slug):
    category_slug = category__slug
    return True


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
