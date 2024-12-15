import time
import pygame

from src.objects.asteroid import Asteroid
from src.objects.asteroid_field import AsteroidField
from src.objects.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    GAME_FPS,
    FONT_SIZE,
    SCORE_POSITION,
    LIVES_POSITION, HEART_ICON_PATH,
)
from src.objects.explosion import Explosion
from src.objects.player import Player
from src.objects.shot import Shot
from src.ui.game_over_menu import GameOverMenu


class Game:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME
        )
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, FONT_SIZE)

        self.heart_icon: pygame.Surface = pygame.image.load(HEART_ICON_PATH).convert_alpha()
        self.heart_icon = pygame.transform.scale(self.heart_icon, (30, 30))

        pygame.display.set_caption("Asteroids")

        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()

        Asteroid.containers = (self.asteroids, self.updatable, self.drawable)
        AsteroidField.containers = self.updatable
        AsteroidField()

        Player.containers = (self.updatable, self.drawable)
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        Explosion.containers = (self.updatable, self.drawable)
        Shot.containers = (self.shots, self.updatable, self.drawable)

        self.dt = 0

    def start(self) -> None:
        self.loop()
        pygame.quit()

    def loop(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            self.screen.fill("black")

            for obj in self.updatable:
                obj.update(self.dt)

            for asteroid in self.asteroids:
                if asteroid.collides_with(self.player):
                    self.player.hit(self.asteroids)
                    if self.player.lives == 0:
                        game_over_menu = GameOverMenu(self.screen, self.player)
                        game_over_menu.loop()
                        return

                for shot in self.shots:
                    if asteroid.collides_with(shot):
                        asteroid.split()
                        self.player.add_score(asteroid.kind)
                        shot.kill()

                for other_asteroid in self.asteroids:
                    if asteroid == other_asteroid:
                        continue

                    if asteroid.position.distance_to(other_asteroid.position) < 0:
                        continue

                    if (
                        asteroid.position.x > SCREEN_WIDTH
                        or asteroid.position.y > SCREEN_HEIGHT
                        or asteroid.position.x < 0
                        or asteroid.position.y < 0
                    ):
                        continue

                    if (
                        time.time() - asteroid.spawned_at < 1.5
                        or time.time() - other_asteroid.spawned_at < 1.5
                    ):
                        continue

                    if asteroid.collides_with(other_asteroid):
                        asteroid.split()
                        other_asteroid.split()

            for obj in self.drawable:
                obj.draw(self.screen)

            for i in range(self.player.lives):
                self.screen.blit(self.heart_icon, (LIVES_POSITION[0] + i * 35, LIVES_POSITION[1]))

            score_text = self.font.render(f"Score: {self.player.score}", True, "white")
            self.screen.blit(score_text, SCORE_POSITION)

            self.dt = self.clock.tick(GAME_FPS) / 1000
            pygame.display.flip()
