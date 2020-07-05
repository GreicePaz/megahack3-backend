# Generated by Django 2.2.13 on 2020-07-05 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grantor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('notification', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'grantors',
            },
        ),
        migrations.CreateModel(
            name='ProductsMeli',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, null=True)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.CharField(max_length=1024, null=True)),
                ('url', models.CharField(max_length=1024)),
            ],
            options={
                'db_table': 'products_meli',
            },
        ),
        migrations.AddField(
            model_name='needbill',
            name='image_pay',
            field=models.CharField(default=1, max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ong',
            name='account',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ong',
            name='agency',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ong',
            name='bank',
            field=models.CharField(default='caixa_economica_federal', max_length=50),
        ),
        migrations.AddField(
            model_name='ong',
            name='cause',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Tag'),
        ),
        migrations.AddField(
            model_name='ong',
            name='email',
            field=models.EmailField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ong',
            name='logo',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='ong',
            name='password',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='NeedVoluntary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
                ('form', models.CharField(default='online', max_length=10)),
                ('active', models.BooleanField(default=True)),
                ('date_register', models.DateTimeField(auto_now_add=True)),
                ('ong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Ong')),
                ('tags', models.ManyToManyField(to='api.Tag')),
            ],
            options={
                'db_table': 'needs_voluntary',
            },
        ),
        migrations.CreateModel(
            name='ContributionVoluntary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grantor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Grantor')),
                ('need', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.NeedVoluntary')),
            ],
            options={
                'db_table': 'contributions_voluntary',
            },
        ),
        migrations.CreateModel(
            name='ContributionProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('purchase_id', models.CharField(max_length=1024)),
                ('grantor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Grantor')),
                ('need', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.NeedProduct')),
            ],
            options={
                'db_table': 'contributions_product',
            },
        ),
        migrations.CreateModel(
            name='ContributionAmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchase_id', models.CharField(max_length=1024)),
                ('grantor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Grantor')),
                ('need', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.NeedBill')),
            ],
            options={
                'db_table': 'contributions_amount',
            },
        ),
        migrations.AddField(
            model_name='needproduct',
            name='product_meli',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.ProductsMeli'),
            preserve_default=False,
        ),
    ]