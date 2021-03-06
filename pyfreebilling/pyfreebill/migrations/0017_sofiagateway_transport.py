# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-10 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyfreebill', '0016_auto_20170208_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='sofiagateway',
            name='transport',
            field=models.CharField(choices=[(b'udp', 'UDP'), (b'tcp', 'TCP'), (b'tls', 'TLS')], default=b'udp', help_text='Which transport to use for register', max_length=15, verbose_name='SIP transport'),
        ),
    ]
