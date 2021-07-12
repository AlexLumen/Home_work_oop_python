from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__()
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Rectangle side cannot be 0 and less than 0")
        self.__side_a = abs(side_a)
        self.__side_b = abs(side_b)
        self._area = round(self.__side_a * self.__side_b, 2)
        self._perimeter = round((self.__side_a + self.__side_b) * 2, 2)
        self._name = 'Rectangle'
