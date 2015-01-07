# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('postindex', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('disctrict', models.CharField(max_length=13, blank=True)),
                ('street', models.CharField(max_length=255)),
                ('numbuild', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
