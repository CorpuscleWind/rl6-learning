# coding=utf-8
from django import forms
from django.core.exceptions import ValidationError
from feedback.models import Feedback


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ['question_1', 'question_2', 'question_3', 'question_4', 'discipline']

    def __init__(self, user, **kwargs):
        self.user = user
        super(FeedbackForm, self).__init__(**kwargs)

    def clean(self):
        cleaned_data = super(FeedbackForm, self).clean()
        print cleaned_data
        if Feedback.objects.filter(user=self.user, discipline=cleaned_data['discipline']).exists():
            raise ValidationError(u'Вы уже осталяли обратную связь о предмете')
        return cleaned_data

    def save(self, commit=True):
        instance = super(FeedbackForm, self).save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance
