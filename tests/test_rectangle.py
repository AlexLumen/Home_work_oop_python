import pytest
from src.Rectangle import Rectangle
from tests.conftest import square


def test_rectangle_creation():
    """Check creating rectangle with attributes 0 or less 0"""
    with pytest.raises(ValueError):
        Rectangle(side_a=0, side_b=5)
    with pytest.raises(ValueError):
        Rectangle(side_a=5, side_b=0)
    with pytest.raises(ValueError):
        Rectangle(side_a=-1, side_b=5)
    with pytest.raises(ValueError):
        Rectangle(side_a=5, side_b=-1)


def test_rectangle_has_name(rectangle):
    """Rectangle has attribute name"""
    assert Rectangle.get_name(rectangle) == 'Rectangle', \
        "Rectangle's name is missing or incorrect"


def test_rectangle_area_is_correct(rectangle):
    """Checking the calculation of the area of a rectangle"""
    assert Rectangle.get_area(rectangle) == 10, \
        "Rectangle's area incorrect"


def test_rectangle_perimeter_is_correct(rectangle):
    """Checking the calculation of the perimeter of a rectangle"""
    assert Rectangle.get_perimeter(rectangle) == 14, \
        "Rectangle's perimeter incorrect"


def test_rectangle_add_area_square(rectangle, square):
    """Checking the calculation areas sum rectangle and square"""
    assert rectangle.add_area(square) == 26.0, \
        "Area's sum incorrect"


def test_rectangle_add_area_invalid_class(rectangle, circle):
    """Checking add area invalid class"""
    with pytest.raises(ValueError):
        rectangle.add_area(square)
