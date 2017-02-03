from django.conf.urls import url
from feedback.views import FeedbackView

urlpatterns = [
    url(r'^$', FeedbackView.as_view(), name='feedback'),
]
