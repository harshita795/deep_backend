import pygame
import sys
from logger import log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")

    # Initialize the sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Assign the containers to the classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable) 

    # AsteroidField only needs to update its timer (it shouldn't be drawn or grouped with asteroids)
    AsteroidField.containers = (updatable,)

    clock = pygame.time.Clock()
    dt = 0.0

    # Calculate the center points of the screen
    center_x = SCREEN_WIDTH / 2
    center_y = SCREEN_HEIGHT / 2

    # Instantiate (create) objects
    player = Player(center_x, center_y)
    asteroid_field = AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update positions of all game objects
        for obj in updatable:
            obj.update(dt)

        # Check for collisions immediately after movement updates
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit() # Shuts down the game window instantly

        screen.fill("black")

        # Draw all objects inside the drawable group dynamically
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
