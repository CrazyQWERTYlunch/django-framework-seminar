from django.urls import path
from seminar_app2.views import index, had_and_tales, dice, one_to_hundred, authors_view, posts_view

app_name = 'seminar_app2'

urlpatterns = [
    path('', index, name='index'),
    path('had/', had_and_tales, name='had_and_tales'),
    path('dice/', dice, name='dice'),
    path('one/', one_to_hundred, name='one_to_hundred'),
    path('authors/', authors_view, name='authors_view'),
    path('posts/', posts_view, name='posts_view'),
]