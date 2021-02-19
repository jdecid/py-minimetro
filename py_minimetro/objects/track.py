from typing import List, Dict

from py_minimetro.objects.station import Station
from py_minimetro.objects.train import Train
from py_minimetro.objects.types.colors import Color


class Track:
    def __init__(self, color: Color):
        self.color: Color = color

        self.link_previous: Dict[Station, Station] = dict()
        self.link_next: Dict[Station, Station] = dict()

        self.trains: List[Train] = []

    def get_next_station(self, station: Station, forward: bool) -> Station:
        if forward:
            return self.link_next[station]
        else:
            return self.link_previous[station]
