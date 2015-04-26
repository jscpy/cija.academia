# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0007_auto_20150426_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capitulo',
            name='objetivo',
            field=django_markdown.models.MarkdownField(),
        ),
    ]
