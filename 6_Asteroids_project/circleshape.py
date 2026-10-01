import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float) -> None:
      
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None:
        pass

    def update(self, dt: float) -> None:
        pass

    def collides_with(self, other) -> None:
        # Measure the distance between the center positions of both objects
        distance = self.position.distance_to(other.position)
        
        # Check if that distance is less than or equal to their combined sizes
        return distance <= (self.radius + other.radius)

    def wrap_around(self) -> None:
        """
        Checks if the object has drifted off the screen boundaries
        and wraps its position to the opposite side.
        """

        # Horizontal wrapping
        if self.position.x < -self.radius:
            self.position.x = SCREEN_WIDTH + self.radius
        elif self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius

        # Vertical wrapping
        if self.position.y < -self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius
        elif self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = -self.radius
