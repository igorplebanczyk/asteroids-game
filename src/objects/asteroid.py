import random

import pygame

from src.objects.circle_shape import CircleShape
from src.objects.constants import *
from src.objects.explosion import Explosion


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, kind):
        super().__init__(x, y, radius)
        self.kind: AsteroidKind = kind

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        Explosion(self.position.x, self.position.y, self.radius)

        if self.radius < ASTEROID_MIN_RADIUS or self.kind == AsteroidKind.SMALL:
            return

        angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(angle)
        vector2 = self.velocity.rotate(-angle)

        radius = self.radius - ASTEROID_MIN_RADIUS
        new_kind = None

        match self.kind:
            case AsteroidKind.LARGE:
                new_kind = AsteroidKind.MEDIUM
            case AsteroidKind.MEDIUM:
                new_kind = AsteroidKind.SMALL

        Asteroid(self.position.x, self.position.y, radius, new_kind).velocity = vector1 * 1.2
        Asteroid(self.position.x, self.position.y, radius, new_kind).velocity = vector2 * 1.2
