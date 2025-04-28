from django.urls import path
from . import views

app_name = 'pokemon'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:national_dex_number>/', views.detail, name='detail'),
    path('caught/', views.caught, name='caught'),
    #path('pokemon/<int:pokemon_id>/', views.pokemon_detail, name='pokemon_detail'),
    #path('games/', views.game_list, name='game_list'),
    #path('games/<int:game_id>/', views.game_detail, name='game_detail'),
]