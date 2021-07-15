# Generated by Django 3.2.5 on 2021-07-15 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_simple_coupons', '0001_initial'),
        migrations.swappable_dependency(settings.DSC_AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='allowedusersrule',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.DSC_AUTH_USER_MODEL, verbose_name='Users'),
        ),
        migrations.AlterField(
            model_name='couponuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.DSC_AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
