# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 05:25
from __future__ import unicode_literals

from django.db import migrations, models
import personagem.models


class Migration(migrations.Migration):

    dependencies = [
        ('personagem', '0002_auto_20170416_0146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('imagem', models.ImageField(upload_to=personagem.models.user_directory_path_capa)),
                ('ativo', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Personagem',
                'verbose_name_plural': 'Personagens',
            },
        ),
    ]
