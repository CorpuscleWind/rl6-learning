# coding=utf-8
from __future__ import unicode_literals

import random

from application.utils import get_part_string
from core.base import update_filename
from core.models import User
from django.db import models
from django.db.models import Prefetch
from django.utils import timezone


class Discipline(models.Model):

    name = models.CharField(u'Название дисциплины', max_length=255)
    short_description = models.TextField(u'Короткое описание')
    image = models.ImageField(upload_to=update_filename('discipline'))

    class Meta:
        verbose_name = u'Дисциплина'
        verbose_name_plural = u'Дисциплины'

    def __unicode__(self):
        return unicode(self.name)


class Test(models.Model):

    name = models.CharField(u'Название теста', max_length=255)
    short_description = models.TextField(u'Короткое описание')
    image = models.ImageField(upload_to=update_filename('test'))
    discipline = models.ForeignKey('Discipline', verbose_name=u'Дисциплина')
    is_active = models.BooleanField(u'Активен сейчас?', default=False)

    class Meta:
        verbose_name = u'Тест'
        verbose_name_plural = u'Тесты'

    def __unicode__(self):
        return unicode(self.name)


class QuestionManager(models.Manager):

    def get_questions_by_user_result(self, user_result):
        question_id_list = QuestionResult.objects.filter(result=user_result).values_list('question_id')
        return self.filter(id__in=question_id_list).prefetch_related(Prefetch('answer_set')).order_by('number')


class Question(models.Model):

    TEXT = 1
    CHOICE = 2

    TYPES = (
        (1, u'Ответ текстом'),
        (2, u'Выбор одного ответа')
    )

    text = models.TextField(u'Текст вопросса')
    number = models.PositiveIntegerField(u'Номер вопроса')
    image = models.ImageField(upload_to=update_filename('question'), null=True, blank=True)
    test = models.ForeignKey('Test')
    type = models.PositiveIntegerField(choices=TYPES, default=TEXT)
    right_answer = models.TextField(u'Текст верного ответа', null=True, blank=True)

    objects = QuestionManager()

    class Meta:
        verbose_name = u'Вопрос'
        verbose_name_plural = u'Вопросы'

    @staticmethod
    def get_type_dict():
        return {
            'open_question': Question.TEXT,
            'choice_question': Question.CHOICE
        }

    def has_image(self):
        print self.image
        return False

    def __unicode__(self):
        return get_part_string(self.text)


class Answer(models.Model):

    text = models.TextField(u'Текст ответа')
    is_correct = models.BooleanField(u'Верный?', default=False)
    question = models.ForeignKey(Question, verbose_name=u'Вопрос')
    image = models.ImageField(upload_to=update_filename('answer'), null=True, blank=True)

    class Meta:
        verbose_name = u'Вариант ответа'
        verbose_name_plural = u'Варианты ответов'

    def __unicode__(self):
        return get_part_string(self.text)


class UserResultManager(models.Manager):

    def get_or_create_user_result(self, test_id, user):
        user_result = UserResult.objects.filter(test_id=test_id, user=user).first()
        if user_result is None:

            questions = Question.objects.filter(test_id=test_id).only('id', 'number')
            question_by_number_dict = dict()
            for question in questions:
                num = question.number
                if num not in question_by_number_dict:
                    question_by_number_dict.update({num: list()})
                question_by_number_dict.get(num).append(question.id)

            question_id_list = list()
            for key, value in question_by_number_dict.iteritems():
                question_id_list.append(random.choice(value))

            user_result = self.create(user=user, test_id=test_id, question_count=len(question_by_number_dict.keys()))
            question_result_list = list()
            for question_id in question_id_list:
                question_result_list.append(QuestionResult(result=user_result, question_id=question_id))

            QuestionResult.objects.bulk_create(question_result_list)

        return user_result


class UserResult(models.Model):

    user = models.ForeignKey(User, verbose_name=u'Пользователь')
    test = models.ForeignKey(Test, verbose_name=u'Тест')
    score = models.PositiveIntegerField(default=0)
    question_count = models.PositiveIntegerField(default=0)
    complete = models.BooleanField(default=False)
    start_time = models.DateTimeField(u'Время начала теста', default=timezone.now)
    end_time = models.DateTimeField(u'Время окончания теста', null=True, blank=True)

    objects = UserResultManager()

    class Meta:
        verbose_name = u'Результат теста'
        verbose_name_plural = u'Результаты тестов'

    def __unicode__(self):
        return unicode(self.user.get_short_name())


class QuestionResult(models.Model):

    result = models.ForeignKey(UserResult, verbose_name=u'Результат пользователя')
    question = models.ForeignKey(Question, verbose_name=u'Вопрос')
    answer = models.TextField(u'Ответ пользователя', null=True, blank=True)
    is_correct = models.BooleanField(u'Верный ответ?', default=False)

    class Meta:
        verbose_name = u'Результат вопроса'
        verbose_name_plural = u'Результаты вопросов'

    def __unicode__(self):
        return unicode(self.result.user.get_short_name())


class Material(models.Model):

    file = models.FileField(upload_to=update_filename('material'))
    name = models.CharField(u'Имя файла', max_length=256)
    description = models.TextField(u'Описание', null=True, blank=True)
    discipline = models.ForeignKey(Discipline, verbose_name=u'Дисциплина')

    class Meta:
        verbose_name = u'Полезный материал'
        verbose_name_plural = u'Полезные материалы'

    def __unicode__(self):
        return unicode(self.name)
