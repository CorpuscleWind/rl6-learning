from django.conf.urls import url
from core.views import IndexView, AuthView, RegistrationView, LogoutView, DomainValidateView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^auth/$', AuthView.as_view(), name='auth'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^registration/$', RegistrationView.as_view(), name='registration'),
    # url(r'^0b9665pg7334f5w6.php', DomainValidateView.as_view(), name='domain_validate'),
]
