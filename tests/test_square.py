import pytest

from src.Square import Square
from tests.conftest import triangle


def test_square_creation():
    """Check creating square with attributes 0 or less 0"""
    with pytest.raises(ValueError):
        Square(side=0)
    with pytest.raises(ValueError):
        Square(side=-1)


def test_square_has_name(square):
    """Square has attribute name"""
    assert Square.get_name(square) == 'Square', \
        "Square's name is missing or incorrect"


def test_square_area_is_correct(square):
    """Checking the calculation of the area of a square"""
    assert Square.get_area(square) == 16, \
        "Rectangle's area incorrect"


def test_square_perimeter_is_correct(square):
    """Checking the calculation of the perimeter of a square"""
    assert Square.get_perimeter(square) == 16, \
        "Rectangle's perimeter incorrect"


def test_square_add_area_triangle(square, triangle):
    """Checking the calculation areas sum square and triangle"""
    assert square.add_area(triangle) == 22.5, \
        "Area's sum incorrect"


def test_square_add_area_invalid_class(square, rectangle):
    """Checking add area invalid class"""
    with pytest.raises(ValueError):
        square.add_area(triangle)
