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
    generation = models.IntegerField()
    PokemonGame = models.ForeignKey('PokemonGame', on_delete=models.CASCADE, related_name='pokemons')

class PokemonGame(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.IntegerField()
    region = models.CharField(max_length=100)
    generation = models.IntegerField()
    def __str__(self):
        return self.name
    def get_generation(self):
        return self.generation