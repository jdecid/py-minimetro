import random
from random import randrange
from typing import List

from py_minimetro.game import Game
from py_minimetro.objects.station import Station
from py_minimetro.objects.types.shapes import Shape


class Minimetro(Game):
    def __init__(self, *args, **kwargs):
        self.__num_stations = 0
        self.__station_spawn_interval = 5

        self.__stations: List[Station] = []

        super().__init__(*args, **kwargs)

    def update(self):
        self.__generate_stations()
        self.__generate_passengers()

    def __generate_stations(self):
        if self._delta_time > self.__station_spawn_interval * self.__num_stations:
            # Random coordinates
            x_coord = randrange(5, self._w_size[0] - 5)
            y_coord = randrange(5, self._w_size[1] - 5)
            coords = (x_coord, y_coord)

            # Random shape
            shape = random.choice(list(Shape))

            new_station = Station(shape=shape, coords=coords)
            text = self._font.render(shape.value, False, (0, 0, 0))
            self._screen.blit(text, coords)

            self.__stations.append(new_station)
            self.__num_stations += 1

    def __generate_passengers(self):
        pass


if __name__ == '__main__':
    game = Minimetro(title='Minimetro', w_size=(256, 128))
