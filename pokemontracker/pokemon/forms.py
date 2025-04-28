from django import forms
from .models import Pokemon, PokemonGame, Platform

class PokemonNewForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['name', 'national_dex_number', 'type1', 'type2', 'legendary', 'generation', 'PokemonGame', 'picture', 'notes']
    
    name = forms.CharField(max_length=100, label='Name')
    national_dex_number = forms.IntegerField(label='National Dex Number')
    type1 = forms.CharField(max_length=50, label='Type 1')
    type2 = forms.CharField(max_length=50, label='Type 2', required=False)
    legendary = forms.BooleanField(label='Legendary', required=False)
    generation = forms.IntegerField(label='Generation')
    PokemonGame = forms.ModelMultipleChoiceField(
        queryset=PokemonGame.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Games'
    )
    picture = forms.ImageField(label='Picture', required=False)
    notes = forms.CharField(widget=forms.Textarea, label='Notes', required=False)