from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.views.generic import ListView, DetailView, RedirectView

from .models import Question, Choice
# Logging 추가
import logging
logger = logging.getLogger(__name__)


# def index(request):
#     latests_question_list = Question.objects.all().order_by('-pub_date')[:5]
#     context = {'latests_question_list': latests_question_list}
#     return render(request, 'polls/index.html', context)

class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latests_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = {'question': question}
#     return render(request, 'polls/detail.html', context)

class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

class ResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': '선택하지 않았습니다!'
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class VoteView(RedirectView):
    pattern_name = 'polls:detail'

    def post(self, request, *args, **kwargs):



        question = get_object_or_404(Question, pk=kwargs['pk'])
        try:
            question_id = request.POST['choice']
            selected_choice = question.choice_set.get(pk=question_id)

        except (KeyError, Choice.DoesNotExist):
            # 로그 기록(실패 시)
            logger.debug(f"vote() without question_id(choice)!")

            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': '선택하지 않았습니다!'
            })
        else:
            # 로그 기록(성공 시)
            logger.debug(f"vote().question_id: {question_id}")

            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
