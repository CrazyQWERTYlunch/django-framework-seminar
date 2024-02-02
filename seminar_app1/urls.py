from django.urls import path
from .views import index, had_and_tales, dice, one_to_hundred

app_name = 'seminar_app1'

urlpatterns = [
    path('', index, name='index'),
    path('had/', had_and_tales, name='had_and_tales'),
    path('dice/', dice, name='dice'),
    path('one/', one_to_hundred, name='one_to_hundred')
]