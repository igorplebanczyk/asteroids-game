import pygame
import random

from src.objects.circle_shape import CircleShape


class Explosion(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.life = 0.5
        self.max_radius = radius
        self.explosion_colors = [
            (255, 69, 0),    # Orange-Red
            (255, 140, 0),   # Dark Orange
            (255, 215, 0),   # Gold
            (255, 255, 0),   # Yellow
        ]

    def update(self, dt):
        self.life -= dt
        if self.life <= 0:
            self.kill()

    def draw(self, screen):
        # The explosion fades as life decreases
        alpha = int(255 * (self.life / 0.5))  # Fading from 255 to 0

        # The explosion progresses outwards by increasing the radius over time
        expansion_factor = 1 - (self.life / 0.5)  # Goes from 0 to 1 as life decreases

        for i in range(8):
            # Random radius factor for each circle in the explosion
            radius_factor = random.uniform(0.3, 1.0)
            # Scale UP the radius over time
            current_radius = int(self.max_radius * radius_factor * expansion_factor)

            # Random color for each ring
            color = random.choice(self.explosion_colors)

            # Random origin offsets for each circle (small jitter)
            x_offset = random.randint(-5, 5)
            y_offset = random.randint(-5, 5)

            # Create a surface to draw on with per-pixel alpha transparency
            explosion_surface = pygame.Surface((self.max_radius * 2, self.max_radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(
                explosion_surface,
                (*color, alpha),  # Apply alpha for fading
                (self.max_radius + x_offset, self.max_radius + y_offset),  # Draw with random offsets
                current_radius,
                2
            )

            # Blit the explosion surface onto the main screen at the correct position
            screen.blit(explosion_surface, (self.position[0] - self.max_radius, self.position[1] - self.max_radius))