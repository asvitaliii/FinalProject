from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.contrib.auth.models import AbstractUser


class UserManager(BaseUserManager):
    def create_user(self, name: str, password: None, is_staff=False, is_admin=False):
        if not name:
            raise ValueError('Нужно задать имя')
        elif not password:
            raise ValueError('Нужно задать пароль')
        else:
            user = self.model(name=name)
            user.set_password(password)
            user.staff = is_staff
            user.admin = is_admin
            user.save(using=self._db)
            return user

    def create_staffuser(self, name, password=None):
        user = self.create_user(
            name,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, name, password=None):
        user = self.create_user(
            name,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user


class MyUser(AbstractBaseUser):
    name = models.CharField(max_length=16)
    active = models.BooleanField(default=False)
    telegram_id = models.CharField(max_length=16)
    targets = dict()

    USERNAME_FIELD = 'name'
    objects = UserManager()

    def set_targets(self, url: str, keywords: str):
        keywords = keywords.split('\n')
        self.targets[url] = keywords

    def set_telegram_id(self, telegram_id):
        self.telegram_id = telegram_id
