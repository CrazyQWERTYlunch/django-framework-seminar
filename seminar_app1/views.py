import logging
from django.shortcuts import render
from django.http import HttpResponse
from random import randint, choice


logger = logging.getLogger(__name__)


def index(request):
    logger.info('index get request')
    return HttpResponse('Hello world!')


def had_and_tales(request):
    answers = ['Heads', 'Tails']
    # return HttpResponse(answers[randint(0, 1)])
    # answer = \
    #     choice(['орёл', 'решка'])
    answer = choice(answers)
    logger.info(f'{__name__} issued a value {answer}')
    return HttpResponse(answer)


def dice(request):
    answer = randint(1, 6)
    logger.info(f'{__name__} issued a value {answer}')
    return HttpResponse(answer)


def one_to_hundred(request):
    answer = randint(1, 100)
    logger.info(f'{__name__} issued a value {answer}')
    return HttpResponse(answer)


