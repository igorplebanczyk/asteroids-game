import pygame

from src.objects.asteroid import Asteroid
from src.objects.asteroid_field import AsteroidField
from src.objects.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    GAME_FPS,
    FONT_SIZE,
    SCORE_TEXT_POSITION,
    LIVES_TEXT_POSITION,
)
from src.objects.explosion import Explosion
from src.objects.player import Player
from src.objects.shot import Shot


class Game:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME
        )
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, FONT_SIZE)

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
                        print("Game over!")
                        print(f"Final score: {self.player.score}")
                        return

                for shot in self.shots:
                    if asteroid.collides_with(shot):
                        asteroid.split()
                        self.player.add_score(asteroid.kind)
                        shot.kill()

            for obj in self.drawable:
                obj.draw(self.screen)

            score_text = self.font.render(f"Score: {self.player.score}", True, "white")
            self.screen.blit(score_text, SCORE_TEXT_POSITION)

            lives_text = self.font.render(f"Lives: {self.player.lives}", True, "white")
            self.screen.blit(lives_text, LIVES_TEXT_POSITION)

            self.dt = self.clock.tick(GAME_FPS) / 1000
            pygame.display.flip()
