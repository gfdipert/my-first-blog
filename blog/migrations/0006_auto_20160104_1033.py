# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160104_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='guides',
            field=models.TextField(default=b'Guide Names'),
        ),
    ]
