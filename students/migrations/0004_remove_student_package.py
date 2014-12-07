# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20141207_2152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='package',
        ),
    ]
