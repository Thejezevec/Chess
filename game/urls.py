from django.urls import path, include
from django.contrib import admin

from .import views

urlpatterns = [
    path('', views.new_game, name='new_game'),
    path('game/<int:game_id>/', views.game_detail, name='game_detail'),
    path('game/<int:game_id>/move/', views.make_move, name='make_move'),

]
