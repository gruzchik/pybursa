# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dossier', '0002_remove_dossier_hate_course'),
        ('coaches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='dossier',
            field=models.OneToOneField(null=True, blank=True, to='dossier.Dossier'),
            preserve_default=True,
        ),
    ]
