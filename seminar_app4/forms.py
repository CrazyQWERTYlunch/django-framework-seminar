import datetime
from seminar_app2.models import Autor, Post

from django import forms


class GameTypeForm(forms.Form):
    game_type = forms.ChoiceField(choices=[
        ('C', 'coins'),
        ('D', 'dice'),
        ('N', 'numbers')]
    )
    throws_number = forms.IntegerField(min_value=1, max_value=64)


# class AuthorAddForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     biography = forms.CharField()
#     birthday = forms.DateField(initial=datetime.date.today())

class AuthorAddForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['name', 'last_name', 'email', 'bio', 'birthday',]


class PostAddFormWidget(forms.Form):
    title = forms.CharField(max_length=50,
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Введите название статьи'}))
    content = forms.CharField(max_length=150,
                              widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Введите текст статьи'}))
    publish_date = forms.DateField(initial=datetime.date.today,
                                   widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    author = forms.ModelChoiceField(queryset=Autor.objects.all())
    is_published = forms.BooleanField(required=False,
                                      widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
