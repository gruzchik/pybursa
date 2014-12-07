# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_remove_student_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='package',
            field=models.CharField(default=b'st', max_length=15),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='package_adv',
            field=models.CharField(default=b'st', max_length=15, choices=[(b'st', b'Standart'), (b'gl', b'Gold'), (b'vp', b'VIP')]),
            preserve_default=True,
        ),
    ]
