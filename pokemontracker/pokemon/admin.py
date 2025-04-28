from django.contrib import admin

from .models import Pokemon, PokemonGame, Platform

class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'national_dex_number', 'type1', 'type2', 'legendary', 'generation')
    search_fields = ('name',)
    list_filter = ('type1', 'type2', 'legendary', 'generation')
    ordering = ('national_dex_number',)

class PokemonGameAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', 'region', 'generation')
    search_fields = ('name',)
    list_filter = ('region', 'generation')
    ordering = ('release_date',)

class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(PokemonGame, PokemonGameAdmin)
admin.site.register(Platform, PlatformAdmin)