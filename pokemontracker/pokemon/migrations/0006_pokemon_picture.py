# Generated by Django 5.2 on 2025-04-28 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0005_pokemon_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='pokemon_pictures/'),
        ),
    ]
