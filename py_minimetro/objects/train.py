from typing import List

from py_minimetro.objects.track import Track
from py_minimetro.objects.wagon import Wagon


class Train:
    def __init__(self, track: Track, wagon: Wagon):
        self.forward: bool = True

        self.track: Track = track
        self.wagons: List[Wagon] = [wagon]

        self.prev_station = None
        self.next_station = None

    def __load_unload(self):
        for wagon in self.wagons:
            wagon.unload_passengers(self.next_station)
            wagon.load_passengers(self.next_station)

    def __advance(self):
        self.prev_station = self.next_station
        self.next_station = self.track.get_next_station(self.next_station)
