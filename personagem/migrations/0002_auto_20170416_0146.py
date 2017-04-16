# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 04:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personagem', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personagem',
            options={'verbose_name': 'Personagem', 'verbose_name_plural': 'Personagens'},
        ),
        migrations.AlterField(
            model_name='personagem',
            name='jogador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]