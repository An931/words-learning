from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(
        _('Email'),
        unique=True
    )
    name = models.CharField(
        _('Name'),
        max_length=30,
        blank=True
    )
    date_joined = models.DateTimeField(_('Registered'), auto_now_add=True)
    is_active = models.BooleanField(_('Is_active'), default=True)
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_('Is staff'),
        help_text=_('The user will have access to admin interface.'),
    )

    objects = UserManager()

    class Meta:
        db_table = 'users'
        ordering = ('-date_joined',)
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return f'{self.email} ({self.name})'

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)
