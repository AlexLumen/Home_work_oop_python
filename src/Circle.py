from src.Figure import Figure
from math import pi


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        if radius <= 0:
            raise ValueError("Radius cannot be 0 and less than 0")
        self.__radius = abs(radius)
        self._area = round(pi * (self.__radius ** 2), 2)
        self._perimeter = round(2 * self.__radius * pi, 2)
        self._name = 'Circle'
