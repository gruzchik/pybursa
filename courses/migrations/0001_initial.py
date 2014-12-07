# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('technology', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('details', models.CharField(max_length=255)),
                ('lector', models.CharField(max_length=255)),
                ('asistant', models.CharField(max_length=255)),
                ('begin_date', models.DateField()),
                ('finish_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
