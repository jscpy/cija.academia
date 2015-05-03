# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0011_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 5, 3, 3, 3, 55, 389910, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
