import pygame
import time

from src.objects.circle_shape import CircleShape
from src.objects.constants import *
from src.objects.shot import Shot


class Player(CircleShape):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation: float = 0.0
        self.shoot_timer: float = 0.0
        self.score: int = 0
        self.lives: int = PLAYER_MAX_LIVES
        self.block_update: bool = False
        self.player_speed: int = PLAYER_SPEED

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.display) -> None:
        pygame.draw.polygon(screen, PLAYER_COLOR, self.triangle(), 0)

    def rotate(self, dt: int) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: int) -> None:
        if self.block_update: return

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
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * self.player_speed * dt

        self.position.x = max(self.radius, min(SCREEN_WIDTH - self.radius, self.position.x))
        self.position.y = max(self.radius, min(SCREEN_HEIGHT - self.radius, self.position.y))

    def shoot(self) -> None:
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN

        shot = Shot(int(self.position.x), int(self.position.y))
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

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


