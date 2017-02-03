# coding=utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, is_staff, is_superuser, is_active, **extra_fields):
        if 'username' in extra_fields:
            del extra_fields['username']

        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=is_staff, is_superuser=is_superuser, is_active=is_active,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, is_active=False, **extra_fields):
        return self._create_user(email, password, False, False, is_active, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(_('first name'), max_length=255)
    last_name = models.CharField(_('last name'), max_length=255)
    email = models.EmailField(_('email address'), unique=True,
                              error_messages={'unique': u'Этот адрес уже используется'})

    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=False,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))

    department = models.ForeignKey('Department', verbose_name=u'Кафедра и группа', null=True, blank=True)

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        swappable = 'AUTH_USER_MODEL'

    def get_short_name(self):
        return u'{0} {1}'.format(self.first_name, self.last_name)

    def get_full_name(self):
        return self.get_short_name()

    def __unicode__(self):
        return self.get_short_name()


class Department(models.Model):
    name = models.CharField(u'Кафедра, группа, год', max_length=255)
    is_active = models.BooleanField('Активна?', default=True)

    class Meta:
        verbose_name = u'Кафедра'
        verbose_name_plural = u'Кафедры'

    def __unicode__(self):
        return unicode(self.name)
