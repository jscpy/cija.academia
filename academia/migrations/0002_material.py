# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('fecha', models.DateField(auto_now=True)),
                ('capitulo', models.ForeignKey(to='academia.Capitulo')),
            ],
        ),
    ]
