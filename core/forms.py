# coding=utf-8
from core.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, ReadOnlyPasswordHashField
from django import forms
from django.utils.translation import ugettext_lazy as _


class UserLoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': u'Неверный email или пароль',
        'inactive': u'Ваш аккаунт не активен',
    }

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = u'E-mail'
        self.fields['password'].widget.attrs['placeholder'] = u'Введите пароль'


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email', 'department'
        ]

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['department'].required = True

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.is_active = True
        if commit:
            user.save()
        return user


class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ()

    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            "Raw passwords are not stored, so there is no way to see this "
            "user's password, but you can change the password using "
            "<a href=\"../password/\">this form</a>."
        ),
    )
