from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.base_user import AbstractBaseUser

class User(AbstractBaseUser):
    USERNAME_FIELD  = 'username'

    username        = models.CharField(max_length=10, unique=True)
    key             = models.CharField(max_length=20)
    is_active       = models.BooleanField(default=True)
    creation_date   = models.DateTimeField(auto_now_add=True)
    password        = None
    class Meta:
        db_table = 'user_project'


class EnumField(models.Field):
    def __init__(self, *args, **kwargs):
        super(EnumField, self).__init__(*args, **kwargs)
        assert self.choices, "Need choices for enumeration"

    def db_type(self, connection):
        return "ENUM({})".format(','.join("'{}'".format(col) for col, _ in self.choices))
    

class Ong(models.Model):
    SANTANDER       = 'santander'
    NUBANK          = 'nubank'
    BRADESCO        = 'bradesco'
    ITAU            = 'itau'
    BANRISUL        = 'banrisul'
    BB              = 'banco_do_brasil'
    CAIXA           = 'caixa_economica_federal'

    TYPE_CHOICES    = 
    (
        (SANTANDER, 'Banco Santander Brasil'),
        (NUBANK, 'Nu Pagamentos S.A.'),
        (BRADESCO, 'Banco Bradesco'),
        (ITAU, 'Banco Itaú Unibanco'),
        (BANRISUL, 'Banrisul'),
        (BB, 'Banco do Brasil'),
        (CAIXA, 'Caixa Econômica Federal'),
    )

    name            = models.CharField(max_length=50)
    logo            = models.CharField(max_length=1024, null=True)
    cnpj            = models.CharField(max_length=20, validators=[MinLengthValidator(14)])
    cause           = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    description     = models.TextField(null=True)
    cep             = models.CharField(max_length=10)
    state           = models.CharField(max_length=30)
    city            = models.CharField(max_length=100, null=True)
    address         = models.CharField(max_length=1024)
    number          = models.IntegerField()
    complement      = models.CharField(max_length=1024, null=True)
    link            = models.CharField(max_length=100, null=True)
    email           = models.EmailField(max_length=100)
    password        = models.CharField(max_length=200)
    bank            = models.EnumField(choices=TYPE_CHOICES, max_length=50, null=True)
    account         = models.CharField(max_length=50, null=True)
    agency          = models.CharField(max_length=50, null=True)
    date_register   = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'ongs'


class Tag(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'tag'


class ProductsMeli(models.Model):
    name    = models.CharField(max_length=1024, null=True)
    value   = models.DecimalField(max_digits=10, decimal_places=2)
    image   = models.CharField(max_length=1024, null=True)
    url     = models.CharField(max_length=1024)
    class Meta:
        db_table = 'products_meli'


class NeedProduct(models.Model):
    name            = models.CharField(max_length=50)
    amount          = models.IntegerField(default=1)
    description     = models.TextField(null=True)
    tags            = models.ManyToManyField('Tag')
    product_meli    = models.ForeignField(ProductsMeli, on_delete=models.CASCADE)
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
    payment_slip    = models.CharField(max_length=1024)
    tags            = models.ManyToManyField('Tag')
    ong             = models.ForeignKey(Ong, on_delete=models.CASCADE)
    active          = models.BooleanField(default=True)
    date_register   = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'needs_bill'


class NeedVoluntary(models.Model):
    PRESENTIAL      = 'presencial'
    ONLINE          = 'online'

    TYPE_CHOICES    = 
    (
        (PRESENTIAL,    'Presencial'),
        (ONLINE,        'Online'),
    )

    role            = models.CharField(max_length=50)
    description     = models.TextField(null=True)
    form            = models.EnumField(choices=TYPE_CHOICES, max_length=10, default=ONLINE)
    tags            = models.ManyToManyField('Tag')
    ong             = models.ForeignKey(Ong, on_delete=models.CASCADE)
    active          = models.BooleanField(default=True)
    date_register   = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'needs_voluntary'


class Grantor(models.Model):
    name            = models.CharField(max_length=100)
    email           = models.EmailField(max_length=100)
    notification    = models.BooleanField(default=True)
    class Meta:
        db_table = 'grantors'


class ContributionVoluntary(models.Model):
    need    = models.ForeignKey(NeedVoluntary, on_delete=models.CASCADE)
    grantor = models.ForeignKey(Grantor, on_delete=models.CASCADE)
    class Meta:
        db_table = 'contributions_voluntary'


class ContributionAmount(models.Model):
    need        = models.ForeignKey(NeedBill, on_delete=models.CASCADE)
    amount      = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_id = models.CharField(max_length=1024)
    grantor     = models.ForeignKey(Grantor, on_delete=models.CASCADE)
    class Meta:
        db_table = 'contributions_amount'


class ContributionProducts(models.Model):
    need        = models.ForeignKey(NeedProduct, on_delete=models.CASCADE)
    amount      = models.IntegerField()
    purchase_id = models.CharField(max_length=1024)
    grantor     = models.ForeignKey(Grantor, on_delete=models.CASCADE)
    class Meta:
        db_table = 'contributions_product'