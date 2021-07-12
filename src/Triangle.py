from src.Figure import Figure
from math import sqrt


class Triangle(Figure):

    def __init__(self, side_base, side_a, side_b):
        super().__init__()
        if side_base <= 0 or side_a <= 0 or side_b <= 0:
            raise ValueError("The side of a triangle cannot be 0 and less than 0")
        elif ((side_base + side_a) < side_b) or ((side_base + side_b) < side_a) or ((side_a + side_b) < side_base):
            raise ValueError("The sum of two sides of a triangle cannot be less than the third side")
        self.__side_base = side_base
        self.__side_a = side_a
        self.__side_b = side_b
        self._area = round(self.__side_base * self.height * 0.5, 2)
        self._perimeter = round(self.__side_a + self.__side_b + self.__side_base, 2)
        self._name = 'Triangle'

    @property
    def semi_perimeter(self):
        """Вычисление полупериметра треугольника для вычисления высоты"""
        semi_perimeter = (self.__side_a + self.__side_b + self.__side_base) / 2
        return semi_perimeter

    @property
    def height(self):
        """Вычисление высоты треугольника для вычисления пощади"""
        height = round((2 * (sqrt(self.semi_perimeter *
                                  (self.semi_perimeter - self.__side_base) *
                                  (self.semi_perimeter - self.__side_a) *
                                  (self.semi_perimeter - self.__side_b)))) / self.__side_base, 2)
        return height
