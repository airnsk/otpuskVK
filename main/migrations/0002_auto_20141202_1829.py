# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zapros',
            name='endYear',
            field=models.IntegerField(null=True, verbose_name=b'endYear', blank=True),
        ),
        migrations.AlterField(
            model_name='zapros',
            name='mdEnd',
            field=models.IntegerField(null=True, verbose_name=b'endDate', blank=True),
        ),
        migrations.AlterField(
            model_name='zapros',
            name='mdStart',
            field=models.IntegerField(null=True, verbose_name=b'startDate', blank=True),
        ),
        migrations.AlterField(
            model_name='zapros',
            name='startYear',
            field=models.IntegerField(null=True, verbose_name=b'startYear', blank=True),
        ),
        migrations.AlterField(
            model_name='zapros',
            name='zarp_apr',
            field=models.IntegerField(null=True, verbose_name=b'apr', blank=True),
        ),
        migrations.AlterField(
            model_name='zapros',
            name='zarp_aug',
            field=models.IntegerField(null=True, verbose_name=b'aug', blank=True),
        ),
        migrations.AlterField(
            model_name='zapros',
            name='zarp_dec',
            field=models.IntegerField(null=True, verbose_name=b'dec', blank=True),
        ),
        migrations.AlterField(
            model_name='zapros',
            name='zarp_feb',
            field=models.IntegerField(null=True, verbose_name=b'feb', blank=True),
        ),
        migrations.AlterField(
            model_name='zapros',
            name='zarp_jan',
            field=models.IntegerField(null=True, verbose_name=b'jan', blank=True),
        ),
        migrations.AlterField(
            model_name='zapros',
            name='zarp_jul',
            field=models.IntegerField(null=True, verbose_name=b'jul', blank=True),
        ),
        migrations.AlterField(
            model_name='zapros',
            name='zarp_jun',
            field=models.IntegerField(null=True, verbose_name=b'jun', blank=True),
        ),
        migrations.AlterField(
            model_name='zapros',
            name='zarp_mar',
            field=models.IntegerField(null=True, verbose_name=b'mar', blank=True),
        ),
        migrations.AlterField(
            model_name='zapros',
            name='zarp_may',
            field=models.IntegerField(null=True, verbose_name=b'may', blank=True),
        ),
        migrations.AlterField(
            model_name='zapros',
            name='zarp_nov',
            field=models.IntegerField(null=True, verbose_name=b'nov', blank=True),
        ),
        migrations.AlterField(
            model_name='zapros',
            name='zarp_oct',
            field=models.IntegerField(null=True, verbose_name=b'oct', blank=True),
        ),
        migrations.AlterField(
            model_name='zapros',
            name='zarp_sep',
            field=models.IntegerField(null=True, verbose_name=b'sep', blank=True),
        ),
    ]
