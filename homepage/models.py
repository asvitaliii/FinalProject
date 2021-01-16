from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.utils.translation import ugettext_lazy as _


# class UserManager(BaseUserManager):
#     def create_user(self, name=None, password=None, is_staff=False, is_admin=False, ):
#         if not name:
#             raise ValueError("Нужно указать имя пользователя")
#         elif not password:
#             raise ValueError("Нужно задать пароль")
#         else:
#             user = self.model(name=name)
#             user.set_password(password)
#             user.staff = is_staff
#             user.admin = is_admin
#             user.save(using=self._db)
#             return user
#
#     def create_staffuser(self, name, password=None):
#         user = self.create_user(
#             name=name,
#             password=password,
#             is_staff=True
#         )
#         return user
#
#     def create_superuser(self, name, password=None):
#         user = self.create_user(
#             name=name,
#             password=password,
#             is_staff=True,
#             is_admin=True
#         )
#         return user


class UserManager(BaseUserManager):
    def create_user(self, name, password, **extra_fields):
        if not name:
            raise ValueError(_('Нужно указать имя пользователя'))
        elif not password:
            raise ValueError(_('Нужно задать пароль'))
        user = self.model(name=name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(name, password, **extra_fields)


class MyUser(AbstractBaseUser):
    name = models.CharField(max_length=16, unique=True)
    active = models.BooleanField(default=False)
    telegram_id = models.CharField(max_length=16)
    targets = dict()

    USERNAME_FIELD = 'name'
    objects = UserManager()

    def set_targets(self, url: str, keywords: str):
        self.targets[url] = keywords.split('\n')

    def set_telegram_id(self, telegram_id):
        self.telegram_id = telegram_id
