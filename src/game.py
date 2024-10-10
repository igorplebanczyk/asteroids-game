import pygame

from src.objects.asteroid import Asteroid
from src.objects.astrofield import AsteroidField
from src.objects.constants import *
from src.objects.player import Player
from src.objects.shot import Shot


def start_game() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    pygame.display.set_caption("Asteroids")

    # Initialize font
    font = pygame.font.Font(None, 36)  # None uses the default font, 36 is the font size

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    _ = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Shot.containers = (shots, updatable, drawable)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                print(f"Score: {player.score}")
                return

            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    player.add_score(asteroid.kind)
                    shot.kill()

        for obj in drawable:
            obj.draw(screen)

        # Draw the score
        score_text = font.render(f"Score: {player.score}", True, "white")
        screen.blit(score_text, (10, 10))  # Position the score at (10, 10)

        dt = clock.tick(60) / 1000
        pygame.display.flip()
