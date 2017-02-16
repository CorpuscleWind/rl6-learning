# coding=utf-8
from django.contrib import admin
from learning.models import Discipline, Test, Answer, Question, UserResult, QuestionResult, Material


class DisciplineAdmin(admin.ModelAdmin):

    list_display = ('name', 'short_description')


class TestAdmin(admin.ModelAdmin):

    list_display = ('name', 'short_description', 'discipline', 'is_active')
    list_filter = ('discipline', )


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 1
    fk_name = 'question'


class QuestionAdmin(admin.ModelAdmin):

    list_display = ('text', 'number', 'type', 'test')
    list_filter = ('test', )
    inlines = (AnswerInline, )


class UserResultAdmin(admin.ModelAdmin):
    list_display = ('test', 'user', 'score', 'question_count', 'complete')
    list_filter = ('test', 'user__department', 'complete')
    search_fields = ('user__first_name', 'user__last_name', 'user__email', )


class QuestionResultAdmin(admin.ModelAdmin):
    list_display = ('question', 'is_correct', 'get_user')
    list_filter = ('result__test', )
    search_fields = ('result__user__first_name', 'result__user__last_name', 'result__user__email', )

    def get_user(self, obj):
        return obj.result.user

    get_user.short_description = U'Пользователь'
    get_user.admin_order_field = 'result__user'


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'discipline')


admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(UserResult, UserResultAdmin)
admin.site.register(QuestionResult, QuestionResultAdmin)
admin.site.register(Material, MaterialAdmin)
