from django.shortcuts import render
from seminar_app4.forms import GameTypeForm, AuthorAddForm, PostAddFormWidget
from seminar_app3.views import heads_and_tales, dice, one_to_hundred
from seminar_app2.models import Autor, Post


def choose_game(request):
    if request.method == 'POST':
        form = GameTypeForm(request.POST)
        if form.is_valid():
            game_type = form.cleaned_data['game_type']
            throws_number = form.cleaned_data['throws_number']
            match game_type:
                case 'C':
                    return heads_and_tales(request, throws_number)
                case 'D':
                    return dice(request, throws_number)
                case _:
                    return one_to_hundred(request, throws_number)

    else:
        form = GameTypeForm()
    return render(request, 'seminar_app4/games.html', {'form': form})


def author_add(request):
    if request.method == "POST":
        form = AuthorAddForm(request.POST)
        message = "Ошибка данных"
        if form.is_valid():
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            biography = form.cleaned_data['bio']
            birthday = form.cleaned_data['birthday']
            author = Autor(name=name, last_name=last_name, email=email, bio=biography, birthday=birthday)
            author.save()
            message = "Автор сохранен"
    else:
        form = AuthorAddForm()
        message = 'Заполните форму'
    return render(request, 'seminar_app4/author_form.html', {'form': form, 'message': message})


def post_add(request):
    if request.method == "POST":
        form = PostAddFormWidget(request.POST)
        message = "Ошибка данных"
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            publish_date = form.cleaned_data['publish_date']
            author = form.cleaned_data['author']
            is_published = form.cleaned_data['is_published']
            post = Post(title=title, content=content, publish_date=publish_date, author=author,
                        is_published=is_published)
            post.save()
            message = "Пост сохранен"
    else:
        form = PostAddFormWidget()
        message = 'Заполните форму'

    context = {
        'form': form,
        'message': message
    }

    return render(request, 'homeworks_app4/post_form.html', context=context)

def post_add(request):
    if request.method == "POST":
        form = PostAddFormWidget(request.POST)
        message = "Ошибка данных"
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            publish_date = form.cleaned_data['publish_date']
            author = form.cleaned_data['author']
            is_published = form.cleaned_data['is_published']
            post = Post(title=title, content=content, publish_date=publish_date, author=author,
                        is_published=is_published)
            post.save()
            message = "Пост сохранен"
    else:
        form = PostAddFormWidget()
        message = 'Заполните форму'

    context = {
        'form': form,
        'message': message
    }

    return render(request, 'homeworks_app4/post_form.html', context=context)