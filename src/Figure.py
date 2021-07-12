class Figure:
    _name = None
    _area = None
    _perimeter = None

    def __init__(self):
        self._name = ''
        self._area = 0
        self._perimeter = 0

    def get_perimeter(self):
        """Get figure's perimeter"""
        return self._perimeter

    def get_area(self):
        """Get figure's ares"""
        return self._area

    def get_name(self):
        """Get figure's name"""
        return self._name

    def add_area(self, other_figure):
        """Addition of areas"""
        if isinstance(other_figure, Figure):
            sum_areas = self._area + other_figure._area
            return sum_areas
        else:
            raise ValueError("Wrong class passed")
