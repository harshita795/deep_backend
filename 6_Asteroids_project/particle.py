import pygame
import random
from circleshape import CircleShape

class ExplosionParticle(CircleShape):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, 2)
        
        # Pick a random direction vector
        direction = pygame.Vector2(0, 1).rotate(random.uniform(0, 360))
        # Give it a high initial explosive speed (between 100 and 200 pixels/sec)
        self.velocity = direction * random.uniform(100, 200)
        self.lifetime = 0.4

    def update(self, dt: float) -> None:
        # Move in a straight line
        self.position += self.velocity * dt
        
        # Count down its remaining lifespan
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius)
