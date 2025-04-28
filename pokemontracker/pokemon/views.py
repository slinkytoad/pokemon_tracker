from django.shortcuts import render

from django.http import HttpResponse
from django.urls import path, reverse
from .models import Pokemon, PokemonGame

def index(request):
    pokemons = Pokemon.objects.all()
    context = {
        'pokemons': pokemons,
    }
    return render(request, 'pokemon/index.html', context)