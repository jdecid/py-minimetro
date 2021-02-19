from py_minimetro.objects.types.shapes import Shape


class Passenger:
    def __init__(self, shape: Shape):
        self.shape: Shape = shape
