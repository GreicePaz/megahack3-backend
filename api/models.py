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


class Ong(models.Model):
    name            = models.CharField(max_length=50)
    description     = models.TextField(null=True)
    cep             = models.CharField(max_length=10)
    state           = models.CharField(max_length=30)
    city            = models.CharField(max_length=100, null=True)
    address         = models.CharField(max_length=1024)
    number          = models.IntegerField()
    complement      = models.CharField(max_length=1024, null=True)
    link            = models.CharField(max_length=100, null=True)
    date_register   = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'ongs'

class NeedProduct(models.Model):
    name            = models.CharField(max_length=50)
    amount          = models.IntegerField(default=1)
    description     = models.TextField(null=True)
    id_product      = models.CharField(max_length=100)
    tags            = models.ManyToManyField('Tag')
    ong             = models.ForeignKey(Ong, on_delete=models.CASCADE)
    active          = models.BooleanField(default=True)
    date_register   = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'needs_product'

class NeedBill(models.Model):
    name            = models.CharField(max_length=50)
    description     = models.TextField(null=True)
    expiration      = models.DateField()
    amount          = models.DecimalField(max_digits=10, decimal_places=2)
    tags            = models.ManyToManyField('Tag')
    ong             = models.ForeignKey(Ong, on_delete=models.CASCADE)
    active          = models.BooleanField(default=True)
    date_register   = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'needs_bill'

class Tag(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'tag'