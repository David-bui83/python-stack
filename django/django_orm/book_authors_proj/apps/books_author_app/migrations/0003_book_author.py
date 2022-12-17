# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-19 01:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books_author_app', '0002_author_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default='Jane Austen', on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books_author_app.Author'),
            preserve_default=False,
        ),
    ]