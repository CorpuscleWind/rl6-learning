import os

from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils.crypto import hashlib
from django.views.generic import FormView
from django.utils.deconstruct import deconstructible


class LoginRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

        return redirect('core:index')


class AjaxFormView(FormView):
    def success(self, form, message=''):
        return JsonResponse({'status': 'OK', 'message': message})

    def error(self, form, message=''):
        return JsonResponse({'status': 'ERROR', 'message': message})

    def form_valid(self, form):
        form.save()
        return self.success(form)

    def form_invalid(self, form):
        message = form.errors
        return self.error(form, message)


@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]

        filename = '{}.{}'.format(hashlib.md5(filename.encode('utf-8')).hexdigest(), ext)
        return os.path.join(self.path, filename)

discipline_upload = PathAndRename('discipline')
test_upload = PathAndRename('test')
question_upload = PathAndRename('question')
answer_upload = PathAndRename('answer')
material_upload = PathAndRename('material')

