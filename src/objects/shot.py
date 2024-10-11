import pygame

from src.objects.circle_shape import CircleShape
from src.objects.constants import *


class Shot(CircleShape):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.display) -> None:
        pygame.draw.circle(screen, SHOT_COLOR, self.position, self.radius, 0)

    def update(self, dt: int) -> None:
        self.position += self.velocity * dt
