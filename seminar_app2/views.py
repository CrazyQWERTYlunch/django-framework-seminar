import logging
from random import choice, randint

from django.http import HttpResponse
from django.shortcuts import render
from seminar_app2.models import Coin, Autor, Post

logger = logging.getLogger(__name__)


def index(request):
    logger.info('index get request')
    return HttpResponse('Hello world!')


def had_and_tales(request):
    answer = choice(['Heads', 'Tails'])
    if answer == 'Heads':
        res = 0
    else:
        res = 1
    logger.info(f'{__name__} issued a value {answer}')
    coin = Coin(side=res)
    coin.save()
    result = Coin.get_data(4)
    return HttpResponse(f'{answer}\n {result}')


def dice(request):
    answer = randint(1, 6)
    logger.info(f'{__name__} issued a value {answer}')
    return HttpResponse(answer)


def one_to_hundred(request):
    answer = randint(1, 100)
    logger.info(f'{__name__} issued a value {answer}')
    return HttpResponse(answer)

def authors_view(request):
    authors = Autor.objects.all()

    res_str = '<br>'.join([str(author) for author in authors])

    return HttpResponse(res_str)

def posts_view(request):
    posts = Post.objects.all()

    res_str = '<br>'.join([str(post) for post in posts])

    return HttpResponse(res_str)