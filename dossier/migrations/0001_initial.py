# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dossier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('like_color', models.CharField(default=b'g', max_length=1, choices=[(b'b', b'blue'), (b'g', b'green'), (b'y', b'yellow'), (b'r', b'red')])),
                ('address', models.ForeignKey(to='address.Address')),
                ('hate_course', models.ManyToManyField(to='courses.Course', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
