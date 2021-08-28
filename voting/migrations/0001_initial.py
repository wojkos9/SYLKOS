# Generated by Django 3.2.5 on 2021-08-28 21:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subname', models.CharField(blank=True, default='', max_length=150)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('members', models.ManyToManyField(blank=True, related_name='members', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ImageAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='VotingType',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Voting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('voting_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.votingtype')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('budget', models.DecimalField(decimal_places=2, max_digits=100)),
                ('stage', models.CharField(max_length=50)),
                ('finish_date', models.DateTimeField()),
                ('rating', models.FloatField(blank=True, null=True)),
                ('album', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='model', to='voting.imagealbum')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.group')),
                ('voting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.voting')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('width', models.FloatField(default=100)),
                ('length', models.FloatField(default=100)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='voting.imagealbum')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('rating', models.FloatField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='voting.project')),
                ('voters_dislike', models.ManyToManyField(related_name='voters_dislike', to=settings.AUTH_USER_MODEL)),
                ('voters_like', models.ManyToManyField(related_name='voters_like', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
