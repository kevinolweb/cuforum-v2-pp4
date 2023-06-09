# Generated by Django 3.2.18 on 2023-04-16 17:18

import cloudinary.models
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
            name='CreditUnion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('logo', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='TopicCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Topic Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('summary', models.TextField(blank=True, max_length=500)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('topic_trending', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socialapp.topiccategory')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='topic_like', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Topics',
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socialapp.topic')),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
    ]
