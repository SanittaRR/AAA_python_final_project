from random import randint
from pizza_classes import *


def log(extra):
    """Декоратор, который выводит имя функции и время выполнения"""
    def decorator(function):
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
            print(f'{function.__name__} {extra} {randint(1, 5)}c!')
        return wrapper
    return decorator


def extra_log(sentence):
    """Декоратор принимает шаблон, в который подставляется время"""
    def decorator(function):
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
            print(sentence.format(randint(1, 5)))
        return wrapper
    return decorator


@log('-')
def bake():
    """Готовит пиццу"""
    print('...')


@extra_log('🛵 Доставили за {}с!')
def delivery():
    """Доставляет пиццу"""
    print('...')


@extra_log('🏠 Забрали за {}с!')
def pickup():
    """Самовывоз"""
    print('...')


if __name__ == '__main__':
    bake()
    pickup()
    delivery()
