# Generated by Django 5.1.4 on 2025-04-19 07:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmclub', '0007_playermatch_player1score_playermatch_player2score_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='playerPool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bmclub.player')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bmclub.tournament')),
            ],
        ),
        migrations.CreateModel(
            name='teamPool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bmclub.team')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bmclub.tournament')),
            ],
        ),
    ]
