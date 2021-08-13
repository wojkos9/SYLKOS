# Generated by Django 3.2.5 on 2021-08-13 21:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('voting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='group',
            name='subname',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
    ]
