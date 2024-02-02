from django.shortcuts import render
from seminar_app2.models import Autor, Post
from random import choice, randint


def index(request):
    context = {
        'title': 'Главная страница',
        'content': 'Контент главной страницы'
    }
    return render(request, 'seminar_app3/index.html', context=context)


def about(request):
    context = {
        'title': 'Главная обо мне',
        'content': 'Контент страницы обо мне',
    }
    return render(request, 'seminar_app3/about.html', context=context)


def heads_and_tales(request, count):
    results = [choice(['Heads', 'Tails']) for _ in range(count)]
    context = {
        'title': 'heads_and_tales',
        'results': results,
    }
    return render(request, 'seminar_app3/game.html', context=context)


def dice(request, count):
    results = [randint(1, 6) for _ in range(count)]
    context = {
        'title': 'dice',
        'results': results,
    }
    return render(request, 'seminar_app3/game.html', context=context)


def one_to_hundred(request, count):
    results = [randint(1, 100) for _ in range(count)]
    context = {
        'title': 'one_to_hundred',
        'results': results,
    }
    return render(request, 'seminar_app3/game.html', context=context)


def author_post(request, author_id):
    author = Autor.objects.get(id=author_id)
    posts = Post.objects.filter(author=author)

    context = {
        'author': author,
        'posts': posts
    }
    return render(request, 'seminar_app3/author_post.html', context=context)


def post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'seminar_app3/post.html', context={'post': post})
