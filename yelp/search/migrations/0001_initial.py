# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('b_id', models.CharField(max_length=200)),
                ('b_name', models.CharField(max_length=200)),
                ('b_zipcode', models.IntegerField(max_length=10)),
            ],
        ),
    ]
