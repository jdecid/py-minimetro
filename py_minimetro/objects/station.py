from typing import List, Tuple

from py_minimetro.objects.passenger import Passenger
from py_minimetro.objects.types.shapes import Shape


class Station:
    def __init__(self, shape: Shape, coords: Tuple[int, int]):
        self.shape: Shape = shape
        self.coords: Tuple[int, int] = coords
        self.passengers: List[any] = []
        self.size = 6

    def remove_passenger(self) -> Passenger:
        return self.passengers.pop(0)
