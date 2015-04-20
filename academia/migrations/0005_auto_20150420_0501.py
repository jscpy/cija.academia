# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0004_auto_20150420_0500'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('encabezado', models.CharField(max_length=100)),
                ('fecha', models.DateField(auto_now=True)),
                ('cuerpo', models.TextField()),
                ('usuario', models.ForeignKey(to='academia.Usuario')),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
