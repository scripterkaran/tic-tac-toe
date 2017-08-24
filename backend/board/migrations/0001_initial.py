# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TicTacToe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_created=True)),
                ('stopped', models.DateTimeField(auto_now_add=True)),
                ('player_o', models.ForeignKey(related_name='player_o_games', to=settings.AUTH_USER_MODEL)),
                ('player_x', models.ForeignKey(related_name='player_x_games', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TicTacToeMove',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_created=True)),
                ('position', models.PositiveIntegerField(validators=(django.core.validators.MaxValueValidator(9), django.core.validators.MinValueValidator(0)))),
                ('played_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('tic_tac_toe', models.ForeignKey(related_name='moves', to='board.TicTacToe')),
            ],
        ),
    ]
