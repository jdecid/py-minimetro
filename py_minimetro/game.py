import abc
from typing import Tuple

import pygame


class Game(abc.ABC):
    def __init__(self, title: str, w_size: Tuple[int, int]):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(title)

        self._w_size = w_size
        self._screen = pygame.display.set_mode(w_size)
        self._screen.fill('#F7F2F1')

        self._font = pygame.font.SysFont('Comic Sans MS', 10)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.update()
            pygame.display.flip()

        pygame.quit()

    @property
    def _delta_time(self):
        return pygame.time.get_ticks() / 1000

    @abc.abstractmethod
    def update(self):
        raise NotImplementedError
