import random
import pygame
import math
from src.objects.circle_shape import CircleShape
from src.objects.constants import *
from src.objects.explosion import Explosion

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, kind):
        super().__init__(x, y, radius)
        self.kind: AsteroidKind = kind
        self.vertices = self.generate_rugged_shape()
        self.color = random.choice(ASTEROID_COLORS)

    def generate_rugged_shape(self):
        # Generate a list of points that will form a rough-edged polygon
        num_points = random.randint(10, 15)  # Number of vertices for the polygon
        angle_step = 360 / num_points  # Divide the circle into equal angles
        rugged_vertices = []

        for i in range(num_points):
            angle = angle_step * i  # Current angle in degrees
            angle_rad = math.radians(angle)  # Convert to radians

            # Add a random variation to the radius to create a rugged look
            random_radius = self.radius * random.uniform(0.7, 1.3)

            # Calculate the x and y coordinates based on the angle and the rugged radius
            x = self.position.x + random_radius * math.cos(angle_rad)
            y = self.position.y + random_radius * math.sin(angle_rad)

            rugged_vertices.append((x, y))

        return rugged_vertices

    def draw(self, screen):
        # Draw the asteroid as a polygon using the rugged vertices
        pygame.draw.polygon(screen, self.color, self.vertices, 0)

    def update(self, dt):
        # Move the asteroid and also update its vertices to match the new position
        self.position += self.velocity * dt
        self.vertices = [(x + self.velocity.x * dt, y + self.velocity.y * dt) for x, y in self.vertices]

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

        # Create two new smaller asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, radius, new_kind)
        asteroid1.velocity = vector1 * 1.2

        asteroid2 = Asteroid(self.position.x, self.position.y, radius, new_kind)
        asteroid2.velocity = vector2 * 1.2
