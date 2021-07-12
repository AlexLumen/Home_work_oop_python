from src.Figure import Figure


class Square(Figure):
    def __init__(self, side):
        super().__init__()
        if side <= 0:
            raise ValueError("The side of a square cannot be 0 and less than 0")
        self.__side = side
        self._area = round(self.__side ** 2, 2)
        self._perimeter = round(self.__side * 4, 2)
        self._name = 'Square'
