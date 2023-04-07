from mathTools.math import add, subtract
from mathTools.geom.circle import Circle


def test_add():
    assert add(3, 4) == 7
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(5, 10) == -5


def test_circle():
    c = Circle(5)
    assert round(c.area(), 2) == 78.54
    assert round(c.circumference(), 2) == 31.42
