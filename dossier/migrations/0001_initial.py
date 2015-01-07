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
                ('like_color', models.CharField(default=b'g', max_length=1, choices=[(b'r', b'red'), (b'o', b'orange'), (b'y', b'yellow'), (b'g', b'green'), (b'b', b'blue'), (b'p', b'purple'), (b'w', b'white')])),
                ('address', models.ForeignKey(blank=True, to='address.Address', null=True)),
                ('hate_course', models.ManyToManyField(to='courses.Course', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
