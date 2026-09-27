import pygame
import sys
from logger import log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")

    # Text font systems
    pygame.font.init()
    score_font = pygame.font.SysFont("freesansbold.ttf", 48)
    score = 0
    lives = 3

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

        # Check for player collisions 
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")

                lives -= 1
                if lives <= 0:
                    print("Game over! Out of lives.")
                    sys.exit() 
                else:
                    print(f"Ouch! Lives left: {lives}")
        
        # Check for bullet-to-asteroid collisions
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")

                    shot.kill()

                    # Check how big the asteroid was to award points
                    if asteroid.radius > ASTEROID_MIN_RADIUS * 2:
                        score += 10
                    elif asteroid.radius > ASTEROID_MIN_RADIUS:
                        score += 20
                    else:
                        score += 50

                    asteroid.split()

        screen.fill("black")

        score_surface = score_font.render(f"Score: {score}", True, "white")
        screen.blit(score_surface, (20, 20))

        lives_surface = score_font.render(f"Lives: {lives}", True, "white")
        screen.blit(lives_surface, (20, 80))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
