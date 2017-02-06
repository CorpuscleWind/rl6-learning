# coding=utf-8
from __future__ import unicode_literals

from core.models import User
from django.db import models
from learning.models import Discipline


class Feedback(models.Model):

    user = models.ForeignKey(User, verbose_name=u'Пользователь')
    discipline = models.ForeignKey(Discipline, verbose_name=u'Дисциплина')
    question_1 = models.TextField(u'Первый вопрос?', null=True, blank=True)
    question_2 = models.TextField(u'Второй вопрос?', null=True, blank=True)
    question_3 = models.TextField(u'Третий вопрос???', null=True, blank=True)

    def __unicode__(self):
        return unicode(self.user.get_short_name())