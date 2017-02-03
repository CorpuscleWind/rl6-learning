# coding=utf-8
from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from learning.models import UserResult, Question, QuestionResult, Answer


class UserResultForm(forms.ModelForm):

    class Meta:
        model = UserResult
        fields = []

    def __init__(self, **kwargs):
        self.instance = kwargs.get('instance')
        self.data = kwargs.get('data')
        self.question_result_dist = dict()
        super(UserResultForm, self).__init__(**kwargs)

    def clean(self):
        if self.instance.complete:
            raise ValidationError(u'Вы уже прошли этот тест')

        question_list = Question.objects.get_questions_by_user_result(self.instance)
        question_result_list = QuestionResult.objects.filter(result=self.instance)
        for question_result in question_result_list:
            self.question_result_dist.update({question_result.question_id: question_result})

        score = 0
        for question in question_list:
            try:
                answer = self.data.get(unicode(question.id))
            except Exception:
                raise ValidationError(u'Пожалуйста, введите все ответы')
            if not answer:
                raise ValidationError(u'Пожалуйста, введите все ответы')

            if question.type == Question.TEXT:
                is_correct = answer == question.right_answer
            else:
                is_correct = Answer.objects.filter(question=question, is_correct=True, text=answer).exists()

            score = score + 1 if is_correct else score
            question_result = self.question_result_dist.get(question.id)
            question_result.answer = answer
            question_result.is_correct = is_correct

        self.instance.end_time = timezone.now()
        self.instance.complete = True
        self.instance.score = score

    def save(self, **kwargs):
        for key, value in self.question_result_dist.iteritems():
            value.save()
        return self.instance.save()

