import random

import pygame

from src.objects.asteroid import Asteroid
from src.constants import (
    AsteroidKind,
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ASTEROID_SPAWN_RATE,
)


class AsteroidField(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer: float = 0.0
        self.edges: list[list] = [
            [
                pygame.Vector2(1, 0),
                lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
            ],
            [
                pygame.Vector2(-1, 0),
                lambda y: pygame.Vector2(
                    SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
                ),
            ],
            [
                pygame.Vector2(0, 1),
                lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
            ],
            [
                pygame.Vector2(0, -1),
                lambda x: pygame.Vector2(
                    x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
                ),
            ],
        ]
        self.asteroid_speed_constraints: [int, int] = [40, 100]

    @staticmethod
    def spawn(
        kind: AsteroidKind, position: pygame.Vector2, velocity: pygame.Vector2
    ) -> None:
        asteroid = Asteroid(
            int(position.x), int(position.y), ASTEROID_MIN_RADIUS * kind.value[0], kind
        )
        asteroid.velocity = velocity

    def update(self, dt: int) -> None:
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(*self.asteroid_speed_constraints)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.choice(list(AsteroidKind))
            self.spawn(kind, position, velocity)
