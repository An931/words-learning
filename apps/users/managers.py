from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """Manager for User model"""

    def create_superuser(self, email: str, password: str):
        user = self.create_user(email=email, password=password, name='')
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

    def create_user(self, email: str, password: str, name):
        user = self.model(email=self.normalize_email(email), name=name)
        user.set_password(password)
        user.save()
        return user
