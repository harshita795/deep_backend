import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
from particle import ExplosionParticle

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

        # Generate a collection of jagged points for this specific rock.
        # We will pick 8 points in a circle outline.
        self.points = []
        for i in range(8):
            angle = (i * 45)
            random_offset = radius * random.uniform(0.75, 1.0)
            point_vector = pygame.Vector2(0, 1).rotate(angle)
            self.points.append(point_vector * random_offset)

    def draw(self, screen: pygame.Surface) -> None:
        if self.radius > ASTEROID_MIN_RADIUS * 2:
            color_choice = "red"
        elif self.radius > ASTEROID_MIN_RADIUS:
            color_choice = "orange"
        else:
            color_choice = "yellow"

        # Calculate where the jagged points are relative to the current position.
        # As the asteroid moves, the center position shifts, so we must add the position to our saved points.
        draw_points = []
        for point in self.points:
            draw_points.append(self.position + point)
     
        # Draw the asteroid as an uneven, jagged geometric polygon!
        pygame.draw.polygon(screen, color_choice, draw_points, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

        self.wrap_around()

    def split(self) -> None:
        for _ in range(10):
            ExplosionParticle(self.position.x, self.position.y)

        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid1.velocity = new_velocity1 * 1.2
        asteroid2.velocity = new_velocity2 * 1.2



        
        

