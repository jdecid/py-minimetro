from typing import List

from py_minimetro.constants import WAGON_MAX_CAPACITY
from py_minimetro.objects.passenger import Passenger
from py_minimetro.objects.station import Station


class Wagon:
    def __init__(self):
        self.passengers: List[Passenger] = []

    def load_passengers(self, station: Station):
        while len(self.passengers) < WAGON_MAX_CAPACITY:
            passenger = station.remove_passenger()
            self.passengers.append(passenger)
            # SLEEP PASSENGER_LOAD_TIME

    def unload_passengers(self, station: Station):
        idx = 0
        while idx < len(self.passengers):
            if self.passengers[idx].shape == station.shape:
                self.passengers.pop(idx)
                # SLEEP PASSENGER_LOAD_TIME
            else:
                idx += 1
