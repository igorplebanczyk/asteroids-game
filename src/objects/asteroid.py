import random
import pygame
import math
import time
from src.objects.collision_object import CollisionObject
from src.objects.constants import (
    AsteroidKind,
    ASTEROID_COLORS,
    ASTEROID_RANDOM_NUM_VERTICES_CONSTRAINTS,
    ASTEROID_RANDOM_RADIUS_FACTOR_CONSTRAINTS,
    ASTEROID_RANDOM_SPLIT_ANGLE_CONSTRAINTS,
    ASTEROID_MIN_RADIUS,
)
from src.objects.explosion import Explosion


class Asteroid(CollisionObject):
    def __init__(self, x: int, y: int, radius: int, kind: AsteroidKind) -> None:
        super().__init__(x, y, radius)
        self.kind: AsteroidKind = kind
        self.vertices: list[tuple] = self.generate_rugged_shape()
        self.color: str = random.choice(ASTEROID_COLORS)
        self.spawned_at: time = time.time()

    def generate_rugged_shape(self) -> list[tuple]:
        num_points = random.randint(*ASTEROID_RANDOM_NUM_VERTICES_CONSTRAINTS)
        angle_step = 360 / num_points
        rugged_vertices = []

        for i in range(num_points):
            angle = angle_step * i
            angle_rad = math.radians(angle)

            random_radius = self.radius * random.uniform(
                *ASTEROID_RANDOM_RADIUS_FACTOR_CONSTRAINTS
            )

            x = self.position.x + random_radius * math.cos(angle_rad)
            y = self.position.y + random_radius * math.sin(angle_rad)

            rugged_vertices.append((x, y))

        return rugged_vertices

    def draw(self, screen: pygame.display) -> None:
        pygame.draw.polygon(screen, self.color, self.vertices, 0)

    def update(self, dt: int) -> None:
        self.position += self.velocity * dt
        self.vertices = [
            (x + self.velocity.x * dt, y + self.velocity.y * dt)
            for x, y in self.vertices
        ]

    def split(self) -> None:
        self.kill()
        Explosion(int(self.position.x), int(self.position.y), self.radius)

        if self.radius < ASTEROID_MIN_RADIUS or self.kind == AsteroidKind.SMALL:
            return

        angle = random.uniform(*ASTEROID_RANDOM_SPLIT_ANGLE_CONSTRAINTS)
        vector1 = self.velocity.rotate(angle)
        vector2 = self.velocity.rotate(-angle)

        radius = self.radius - ASTEROID_MIN_RADIUS
        new_kind = None

        match self.kind:
            case AsteroidKind.LARGE:
                new_kind = AsteroidKind.MEDIUM
            case AsteroidKind.MEDIUM:
                new_kind = AsteroidKind.SMALL

        asteroid1 = Asteroid(
            int(self.position.x), int(self.position.y), radius, new_kind
        )
        asteroid1.velocity = vector1 * 1.2

        asteroid2 = Asteroid(
            int(self.position.x), int(self.position.y), radius, new_kind
        )
        asteroid2.velocity = vector2 * 1.2
