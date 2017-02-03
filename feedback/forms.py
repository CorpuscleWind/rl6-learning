from django import forms
from feedback.models import Feedback


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ['question_1', 'question_2', 'question_3', 'discipline']

    def __init__(self, user, **kwargs):
        self.user = user
        super(FeedbackForm, self).__init__(**kwargs)

    def save(self, commit=True):
        instance = super(FeedbackForm, self).save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance
