from django.contrib.auth.models import BaseUserManager
from django.db.models import Q, QuerySet
from django.utils.translation import ugettext_lazy as _


__all__ = (
    'UserManager',
)


class UserManager(BaseUserManager):


    def create_superuser(self, email: str, password: str):
        user = self.create_user(
            email=email, password=password,
        )

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

    def create_user(self, email: str, password: str, name=''):
        # todo
        user = self.model(
            email=self.normalize_email(email),
            name=name
        )
        user.set_password(password)
        user.save()

        return user
