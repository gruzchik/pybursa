# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dossier', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=75)),
                ('phone_number', models.CharField(max_length=13, blank=True)),
                ('package', models.CharField(default=b's', max_length=1, choices=[(b's', b'Standard'), (b'g', b'Gold'), (b'p', b'Platinum')])),
                ('courses', models.ManyToManyField(to='courses.Course', blank=True)),
                ('dossier', models.OneToOneField(null=True, blank=True, to='dossier.Dossier')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
