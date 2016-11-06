# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='zapros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('muser_id', models.CharField(max_length=255, verbose_name=b'userid')),
                ('datezapros', models.DateField(auto_now=True, verbose_name=b'date')),
                ('zarp_jan', models.IntegerField(verbose_name=b'jan', blank=True)),
                ('zarp_feb', models.IntegerField(verbose_name=b'feb', blank=True)),
                ('zarp_mar', models.IntegerField(verbose_name=b'mar', blank=True)),
                ('zarp_apr', models.IntegerField(verbose_name=b'apr', blank=True)),
                ('zarp_may', models.IntegerField(verbose_name=b'may', blank=True)),
                ('zarp_jun', models.IntegerField(verbose_name=b'jun', blank=True)),
                ('zarp_jul', models.IntegerField(verbose_name=b'jul', blank=True)),
                ('zarp_aug', models.IntegerField(verbose_name=b'aug', blank=True)),
                ('zarp_sep', models.IntegerField(verbose_name=b'sep', blank=True)),
                ('zarp_oct', models.IntegerField(verbose_name=b'oct', blank=True)),
                ('zarp_nov', models.IntegerField(verbose_name=b'nov', blank=True)),
                ('zarp_dec', models.IntegerField(verbose_name=b'dec', blank=True)),
                ('mdStart', models.IntegerField(verbose_name=b'startDate', blank=True)),
                ('mdEnd', models.IntegerField(verbose_name=b'endDate', blank=True)),
                ('startYear', models.IntegerField(verbose_name=b'startYear', blank=True)),
                ('endYear', models.IntegerField(verbose_name=b'endYear', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
