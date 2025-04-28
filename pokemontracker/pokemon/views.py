from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse
from django.urls import path, reverse
from .models import Pokemon, PokemonGame, Platform
from .forms import PokemonNewForm

def index(request):
    pokemons = Pokemon.objects.prefetch_related('PokemonGame').filter(caught=True)
    context = {
        'pokemons': pokemons,
    }
    return render(request, 'pokemon/index.html', context)

def detail(request, national_dex_number):
    #pokemon = Pokemon.objects.prefetch_related('PokemonGame').get(id=pokemon_id)
    pokemon = get_object_or_404(Pokemon, national_dex_number=national_dex_number)
    context = {
        'pokemon': pokemon,
    }
    return render(request, 'pokemon/detail.html', context)

def caught(request):
    if request.method == 'POST':
        form = PokemonNewForm(request.POST, request.FILES)
        if form.is_valid():
            pokemon = form.save(commit=False)
            pokemon.PokemonGame = PokemonGame.objects.get(id=request.POST.get('PokemonGame'))
            pokemon.save()
            form.save_m2m()  # Save the many-to-many relationship
            return redirect('pokemon:detail', national_dex_number=pokemon.national_dex_number)
            # return HttpResponseRedirect(reverse('pokemon:detail', args=[pokemon.national_dex_number]))
        else:
            return render(request, 'pokemon/caught.html', {'form': form})
        # pokemon.save()
    else:
        return render(request, 'pokemon/caught.html', {'form': PokemonNewForm()})