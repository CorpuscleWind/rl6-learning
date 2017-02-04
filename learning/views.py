from core.base import AjaxFormView, LoginRequiredMixin
from django.http import Http404
from django.views.generic import TemplateView
from learning.forms import UserResultForm
from learning.models import Test, Discipline, Question, UserResult


class DisciplineView(LoginRequiredMixin, TemplateView):
    template_name = 'discipline/discipline.html'

    def get_context_data(self, **kwargs):
        context = super(DisciplineView, self).get_context_data(**kwargs)
        context['discipline'] = Discipline.objects.filter(id=kwargs.get('discipline_id')).first()
        if not context['discipline']:
            raise Http404
        context['test_list'] = Test.objects.filter(discipline_id=kwargs.get('discipline_id'))
        return context


class TestView(LoginRequiredMixin, TemplateView, AjaxFormView):
    template_name = 'test/test.html'
    form_class = UserResultForm

    def dispatch(self, request, *args, **kwargs):
        test_id = kwargs.get('test_id')
        self.test = Test.objects.filter(id=test_id).first()
        if not self.test or not self.test.is_active:
            raise Http404
        return super(TestView, self).dispatch(request, *args, **kwargs)

    def get_form(self, **kwargs):
        test_id = self.test.id
        user_result = UserResult.objects.get_or_create_user_result(test_id, self.request.user)
        return self.form_class(data=self.request.POST, instance=user_result)

    def get_context_data(self, **kwargs):
        context = super(TestView, self).get_context_data(**kwargs)
        test_id = self.test.id

        context['test'] = self.test
        if not context['test']:
            raise Http404
        context['question_list'] = Question.objects.filter(test_id=test_id)

        user_result = UserResult.objects.get_or_create_user_result(test_id, self.request.user)
        questions = Question.objects.get_questions_by_user_result(user_result)

        context['user_result'] = user_result
        context['question_list'] = questions
        context.update(Question.get_type_dict())

        return context
