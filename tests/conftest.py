import pytest


from src.Circle import Circle
from src.Triangle import Triangle
from src.Rectangle import Rectangle
from src.Square import Square


@pytest.fixture
def triangle():
    triangle = Triangle(3, 5, 7)
    return triangle


@pytest.fixture
def circle():
    circle = Circle(5)
    return circle


@pytest.fixture
def rectangle():
    rectangle = Rectangle(2, 5)
    return rectangle


@pytest.fixture
def square():
    square = Square(4)
    return square
