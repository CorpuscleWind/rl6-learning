from core.base import AjaxFormView, LoginRequiredMixin
from feedback.forms import FeedbackForm
from feedback.models import Feedback


class FeedbackView(LoginRequiredMixin, AjaxFormView):
    form_class = FeedbackForm

    def get_form(self, form_class=None):
        return self.form_class(self.request.user, data=self.request.POST)
