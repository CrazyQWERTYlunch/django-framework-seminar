from django.urls import path
from seminar_app3 import views

app_name = 'seminar_app3'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('game/<int:count>/', views.heads_and_tales, name='heads_and_tales'),
    path('dice/<int:count>/', views.dice, name='dice'),
    path('one_to_hundred/<int:count>/', views.one_to_hundred, name='one_to_hundred'),
    path('author_post/<int:author_id>/', views.author_post, name='author_post'),
    path('post_view/<int:post_id>/', views.post_view, name='post_view'),
]
