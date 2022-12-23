import pytest
from pizza_classes import *


def test_size_type():
    with pytest.raises(TypeError):
        Margherita('X')


def test_equal_pizza():
    """ Проверяет одинаковые ли пиццы"""
    actual = (Margherita('XL') == Margherita('XL'))
    expected = True
    assert actual == expected


def test_not_equal_title():
    """ Проверяет, определяет ли разные названия"""
    actual = (Margherita('XL') == Pepperoni('XL'))
    expected = False
    assert actual == expected


def test_not_equal_size():
    """ Проверяет, определяет ли разные размеры"""
    actual = (Margherita('XL') == Margherita('L'))
    expected = False
    assert actual == expected
