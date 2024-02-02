from django.urls import path
from seminar_app4 import views

app_name = 'seminar_app4'

urlpatterns = [
    path('game/', views.choose_game, name='game'),
    path('author/', views.author_add, name='author'),
    path('post/', views.post_add, name='post'),
]
