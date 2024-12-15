import pygame
import time

from src.objects.collision_object import CollisionObject
from src.constants import (
    PLAYER_SIZE,
    PLAYER_MAX_LIVES,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    PLAYER_SHOOT_COOLDOWN,
    PLAYER_SHOOT_SPEED,
    AsteroidKind,
    PLAYER_RESPAWN_COOLDOWN,
    PLAYER_IMAGE_PATH,
)
from src.objects.shot import Shot


class Player(CollisionObject):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, PLAYER_SIZE)
        self.rotation: float = 0.0
        self.shoot_timer: float = 0.0
        self.score: int = 0
        self.lives: int = PLAYER_MAX_LIVES
        self.block_update: bool = False
        self.player_speed: int = PLAYER_SPEED
        self.image: pygame.Surface = pygame.image.load(PLAYER_IMAGE_PATH)
        self.image = pygame.transform.scale(
            self.image, (2 * PLAYER_SIZE, 2 * PLAYER_SIZE)
        )

    def draw(self, screen: pygame.Surface) -> None:
        rotated_image = pygame.transform.rotate(self.image, -self.rotation)
        rect = rotated_image.get_rect(center=(self.position.x, self.position.y))
        screen.blit(rotated_image, rect.topleft)

    def rotate(self, dt: int) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: int) -> None:
        if self.block_update:
            return

        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_LSHIFT]:
            self.player_speed = PLAYER_SPEED * 2

    def move(self, dt: int) -> None:
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += forward * self.player_speed * dt

        self.position.x = max(
            self.radius, min(SCREEN_WIDTH - self.radius, self.position.x)
        )
        self.position.y = max(
            self.radius, min(SCREEN_HEIGHT - self.radius, self.position.y)
        )

    def shoot(self) -> None:
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN

        shot = Shot(int(self.position.x), int(self.position.y))
        shot.velocity = pygame.Vector2(0, -1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def add_score(self, kind: AsteroidKind) -> None:
        self.score += kind.value[1]

    def hit(self, asteroids: pygame.sprite.Group) -> None:
        self.block_update = True

        self.lives -= 1
        self.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 0
        self.shoot_timer = 0

        for asteroid in asteroids:
            asteroid.kill()

        time.sleep(PLAYER_RESPAWN_COOLDOWN)

        self.block_update = False
