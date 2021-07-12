import pytest
from src.Circle import Circle
from tests.conftest import square


def test_circle_creation():
    """Check creating circle with attributes 0 or less 0"""
    with pytest.raises(ValueError):
        Circle(radius=0)
    with pytest.raises(ValueError):
        Circle(radius=-5)


def test_circle_has_name(circle):
    """Circle has attribute name"""
    assert Circle.get_name(circle) == 'Circle', \
        "Circle's name is missing or incorrect"


def test_circle_area_is_correct(circle):
    """Checking the calculation of the area of a circle"""
    assert Circle.get_area(circle) == 78.54, \
        "Circle's area incorrect"


def test_circle_perimeter_is_correct(circle):
    """Checking the calculation of the perimeter of a circle"""
    assert Circle.get_perimeter(circle) == 31.42, \
        "Circle's perimeter incorrect"


def test_circle_add_area_rectangle(circle, rectangle):
    """Checking the calculation areas sum circle and rectangle"""
    assert circle.add_area(rectangle) == 88.54, \
        "Area's sum incorrect"


def test_circle_add_area_invalid_class(circle, rectangle):
    """Checking add area invalid class"""
    with pytest.raises(ValueError):
        circle.add_area(square)
