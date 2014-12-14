# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_slug'),
        ('dossier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dossier',
            name='hate_course',
            field=models.ManyToManyField(to='courses.Course', null=True, blank=True),
            preserve_default=True,
        ),
    ]
