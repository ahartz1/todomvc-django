# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20151021_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='order',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
