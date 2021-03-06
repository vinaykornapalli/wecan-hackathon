# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-17 18:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='null', verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
        ),
        migrations.AlterField(
            model_name='post',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='post.Branch'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='post.Topic'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='post',
            name='time',
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together=set([('user', 'content')]),
        ),
    ]
