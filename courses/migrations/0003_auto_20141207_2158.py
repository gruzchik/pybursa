# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20141207_0110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='technology',
        ),
        migrations.AddField(
            model_name='course',
            name='technology_adv',
            field=models.CharField(default=b'pybursa', max_length=255, choices=[(b'rubybursa', b'rubybursa'), (b'pybursa', b'pybursa'), (b'phpbursa', b'phpbursa')]),
            preserve_default=True,
        ),
    ]
