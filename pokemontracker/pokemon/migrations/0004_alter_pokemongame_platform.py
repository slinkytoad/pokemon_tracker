# Generated by Django 5.2 on 2025-04-28 20:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0003_remove_pokemon_pokemongame_pokemon_pokemongame'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemongame',
            name='platform',
            field=models.ForeignKey(blank=True, default='5', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='games', to='pokemon.platform'),
        ),
    ]
