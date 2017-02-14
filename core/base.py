import hashlib
from functools import partial

import os

from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic import FormView


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


def update_filename(path):
    def upload(up_path, instance, filename):
        ext = filename.split('.')[-1] if len(filename.split('.')) > 2 else ''
        name = hashlib.md5(filename.encode('utf-8')).hexdigest() + '.' + ext
        return os.path.join(up_path, name)
    return partial(upload, path)
