# Generated by Django 5.2 on 2025-04-28 19:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('region', models.CharField(max_length=100)),
                ('generation', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('national_dex_number', models.IntegerField()),
                ('type1', models.CharField(max_length=50)),
                ('type2', models.CharField(blank=True, max_length=50, null=True)),
                ('legendary', models.BooleanField(default=False)),
                ('generation', models.IntegerField()),
                ('PokemonGame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemons', to='pokemon.pokemongame')),
            ],
        ),
    ]
