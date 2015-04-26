# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0005_auto_20150420_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cuerpo',
            field=django_markdown.models.MarkdownField(),
        ),
    ]
