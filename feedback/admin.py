from django.contrib import admin
from feedback.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('discipline', 'question_1', 'question_2', 'question_3')


admin.site.register(Feedback, FeedbackAdmin)
