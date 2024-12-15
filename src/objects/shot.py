import pygame

from src.objects.collision_object import CollisionObject
from src.constants import SHOT_RADIUS, SHOT_COLOR


class Shot(CollisionObject):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.display) -> None:
        pygame.draw.circle(screen, SHOT_COLOR, self.position, self.radius, 0)

    def update(self, dt: int) -> None:
        self.position += self.velocity * dt
