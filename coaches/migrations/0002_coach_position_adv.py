# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='position_adv',
            field=models.CharField(default=b'Lector', max_length=25, choices=[(b'Lector', b'Lector'), (b'Asistant', b'Asistant')]),
            preserve_default=True,
        ),
    ]
