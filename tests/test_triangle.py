import pytest
from src.Triangle import Triangle
from tests.conftest import square


def test_triangle_creation():
    """Check creating triangle with attributes 0 or less 0 or sum of two sides less than the third side"""
    with pytest.raises(ValueError):
        Triangle(side_base=3, side_a=4, side_b=0)
    with pytest.raises(ValueError):
        Triangle(side_base=0, side_a=6, side_b=4)
    with pytest.raises(ValueError):
        Triangle(side_base=5, side_a=0, side_b=4)
    with pytest.raises(ValueError):
        Triangle(side_base=-1, side_a=4, side_b=5)
    with pytest.raises(ValueError):
        Triangle(side_base=4, side_a=-4, side_b=5)
    with pytest.raises(ValueError):
        Triangle(side_base=4, side_a=6, side_b=-7)
    with pytest.raises(ValueError):
        Triangle(side_base=12, side_a=2, side_b=3)


def test_triangle_has_name(triangle):
    """Triangle has attribute name"""
    assert Triangle.get_name(triangle) == 'Triangle', \
        "Triangle's name is missing or incorrect"


def test_triangle_area_is_correct(triangle):
    """Checking the calculation of the area of a triangle"""
    assert Triangle.get_area(triangle) == 6.5, \
        "Triangle's area incorrect"


def test_triangle_perimeter_is_correct(triangle):
    """Checking the calculation of the perimeter of a triangle"""
    assert Triangle.get_perimeter(triangle) == 15, \
        "Triangle's perimeter incorrect"


def test_triangle_add_area_circle(triangle, circle):
    """Checking the calculation areas sum triangle and circle"""
    assert triangle.add_area(circle) == 85.04, \
        "Area's sum incorrect"


def test_triangle_add_area_invalid_class(triangle, rectangle):
    """Checking add area invalid class"""
    with pytest.raises(ValueError):
        triangle.add_area(square)


def test_triangle_semi_perimeter(triangle):
    """Checking the calculation triangle's semi perimeter"""
    assert triangle.semi_perimeter == 7.5, \
        "Triangle's semi perimeter is incorrect"


def test_triangle_height(triangle):
    """Checking the calculation triangle's semi perimeter"""
    assert triangle.height == 4.33, \
        "Triangle's height is incorrect"
