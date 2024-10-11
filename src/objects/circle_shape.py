import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, radius: int) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.radius: int = radius

    def draw(self, screen: pygame.display) -> None:
        # sub-classes must override
        pass

    def update(self, dt: int) -> None:
        # sub-classes must override
        pass

    def collides_with(self, other) -> bool:
        return self.position.distance_to(other.position) < self.radius + other.radius
