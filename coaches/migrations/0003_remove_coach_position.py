# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0002_coach_position_adv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coach',
            name='position',
        ),
    ]
