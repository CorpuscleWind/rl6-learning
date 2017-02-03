from django.conf.urls import url
from learning.views import DisciplineView, TestView

urlpatterns = [
    url(r'^(?P<discipline_id>\d+)/$', DisciplineView.as_view(), name='discipline'),
    url(r'^test/(?P<test_id>\d+)$', TestView.as_view(), name='test'),
]
