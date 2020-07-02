from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

class User(AbstractBaseUser):
    USERNAME_FIELD = 'username'

    username = models.CharField(max_length=10, unique=True)
    key = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    password = None
    class Meta:
        db_table = 'user_project'
