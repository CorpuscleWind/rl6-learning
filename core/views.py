from core.base import AjaxFormView
from core.forms import UserRegistrationForm, UserLoginForm
from core.models import Department
from django.contrib.auth import login, logout
from django.views.generic import TemplateView, RedirectView
from learning.models import Discipline


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['department_list'] = Department.objects.filter(is_active=True)
        context['discipline_list'] = Discipline.objects.all()
        return context


class RegistrationView(AjaxFormView):
    http_method_names = ['post']
    form_class = UserRegistrationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return self.success(form)


class AuthView(AjaxFormView):
    http_method_names = ['post']
    form_class = UserLoginForm

    def form_valid(self, form):
        login(self.request, form.get_user())
        return self.success(form)


class LogoutView(RedirectView):
    url = '/'
    http_method_names = ['get', 'post']

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)


class DomainValidateView(TemplateView):
    template_name = 'core/domain_validate.html'
