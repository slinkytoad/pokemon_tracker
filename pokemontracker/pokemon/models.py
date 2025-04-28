import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    national_dex_number = models.IntegerField()
    type1 = models.CharField(max_length=50)
    type2 = models.CharField(max_length=50, blank=True, null=True)
    legendary = models.BooleanField(default=False)
    caught = models.BooleanField(default=False)
    generation = models.IntegerField()
    PokemonGame = models.ManyToManyField('PokemonGame', related_name='pokemons')
    picture = models.ImageField(upload_to='pokemon_pictures/', blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name

class PokemonGame(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.IntegerField(blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    generation = models.IntegerField(blank=True, null=True)
    platform = models.ForeignKey('Platform', on_delete=models.CASCADE, blank=True, null=True, related_name='games',default='5')
    def __str__(self):
        return self.name
    def get_generation(self):
        return self.generation

class Platform(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name