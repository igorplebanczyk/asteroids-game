import random
import pygame
import math
import time
from src.objects.collision_object import CollisionObject
from src.constants import (
    AsteroidKind,
    ASTEROID_COLORS,
    ASTEROID_RANDOM_NUM_VERTICES_CONSTRAINTS,
    ASTEROID_RANDOM_RADIUS_FACTOR_CONSTRAINTS,
    ASTEROID_RANDOM_SPLIT_ANGLE_CONSTRAINTS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_NUM_CRATERS_CONSTRAINTS,
    ASTEROID_CRATER_DARKEN_BY,
)
from src.objects.explosion import Explosion


class Asteroid(CollisionObject):
    def __init__(self, x: int, y: int, radius: int, kind: AsteroidKind) -> None:
        super().__init__(x, y, radius)
        self.kind: AsteroidKind = kind
        self.vertices: list[tuple] = self.generate_rugged_shape()
        self.color: tuple = random.choice(ASTEROID_COLORS)
        self.crater_color: tuple = self.darken_color(self.color)
        self.craters: list[tuple] = self.generate_craters()
        self.spawned_at: time = time.time()

    @staticmethod
    def darken_color(color: tuple) -> tuple:
        return tuple(max(int(c * ASTEROID_CRATER_DARKEN_BY), 0) for c in pygame.Color(color))

    def generate_craters(self) -> list[tuple]:
        craters = []
        num_craters = random.randint(*ASTEROID_NUM_CRATERS_CONSTRAINTS)

        base_angle_step = 2 * math.pi / num_craters
        for i in range(num_craters):
            base_angle = i * base_angle_step
            angle = base_angle + random.uniform(-base_angle_step * 0.25, base_angle_step * 0.25)

            distance_from_center = random.uniform(0.25 * self.radius, self.radius)
            crater_radius = random.uniform(0.125 * self.radius, 0.25 * self.radius)

            x = self.position.x + distance_from_center * math.cos(angle)
            y = self.position.y + distance_from_center * math.sin(angle)

            craters.append((x, y, crater_radius))

        return craters

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

        for crater_x, crater_y, crater_radius in self.craters:
            pygame.draw.circle(screen, self.crater_color, (int(crater_x), int(crater_y)), int(crater_radius))

    def update(self, dt: int) -> None:
        self.position += self.velocity * dt
        self.vertices = [
            (x + self.velocity.x * dt, y + self.velocity.y * dt)
            for x, y in self.vertices
        ]
        self.craters = [
            (x + self.velocity.x * dt, y + self.velocity.y * dt, r)
            for x, y, r in self.craters
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
