import pygame
import random
import sys
from logger import log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from particle import ExplosionParticle

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")

    # Create a list of 100 random (X, Y) pixel positions across the screen
    stars = []
    for _ in range(100):
        star_x = random.randint(0, SCREEN_WIDTH)
        star_y = random.randint(0, SCREEN_HEIGHT)
        stars.append((star_x, star_y))

    # Text font systems
    pygame.font.init()
    score_font = pygame.font.Font("freesansbold.ttf", 48)
    score = 0
    lives = 3
    screen_shake_time = 0.0
    game_is_over = False
    damage_flash_time = 0.0

    # Read the all-time high score from a text file once at launch
    high_score = 0
    try: 
        with open("highscore.txt", "r") as file:
            high_score= int(file.read().strip())
    except(FileNotFoundError, ValueError):
        high_score = 0

    # Initialize the sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Assign the containers to the classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable) 
    ExplosionParticle.containers = (updatable, drawable)

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

        # GAME OVER MENU SCREEN
        if game_is_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                # Reset tracking metrics
                lives = 3
                score = 0
                game_is_over = False
                
                # Wipe the operational arrays clean
                for asteroid in asteroids:
                    asteroid.kill()
                for shot in shots:
                    shot.kill()
                    
                player.respawn()

            # Render Menu Graphics Dashboard
            screen.fill("black")
            
            game_over_surface = score_font.render("GAME OVER", True, "red")
            final_score_surface = score_font.render(f"Final Score: {score}", True, "yellow")
            restart_surface = score_font.render("Press ENTER to Restart", True, "white")
            
            screen.blit(game_over_surface, (SCREEN_WIDTH / 2 - game_over_surface.get_width() / 2, SCREEN_HEIGHT / 2 - 80))
            screen.blit(final_score_surface, (SCREEN_WIDTH / 2 - final_score_surface.get_width() / 2, SCREEN_HEIGHT / 2))
            screen.blit(restart_surface, (SCREEN_WIDTH / 2 - restart_surface.get_width() / 2, SCREEN_HEIGHT / 2 + 80))
            
            pygame.display.flip()
            dt = clock.tick(60) / 1000
            continue  # Safety freeze lock: re-run the while loop from the top!


        # Update positions of all game objects
        for obj in updatable:
            obj.update(dt)

        # Check for player collisions 
        for asteroid in asteroids:
            if player.invincible_timer > 0:
                continue
                
            if asteroid.collides_with(player):
                log_event("player_hit")
                lives -= 1
                screen_shake_time = 0.3
                damage_flash_time = 0.1

                if lives <= 0:
                    if score > high_score:
                        high_score = score
                        with open("highscore.txt", "w") as file:
                            file.write(str(high_score))

                    print("Game over! Out of lives.")
                    game_is_over = True
                    break 
                else:
                    player.respawn()
                    print(f"Ouch! Lives left: {lives}")
        
        # Check for bullet-to-asteroid collisions
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    screen_shake_time = 0.15

                    # Check how big the asteroid was to award points
                    if asteroid.radius > ASTEROID_MIN_RADIUS * 2:
                        score += 10
                    elif asteroid.radius > ASTEROID_MIN_RADIUS:
                        score += 20
                    else:
                        score += 50

                    asteroid.split()

        screen.fill("black")

        # Move and wrap stars based on the player's movement velocity
        for i in range(len(stars)):
            star_x, star_y = stars[i]
            star_x -= player.velocity.x * dt * 0.5
            star_y -= player.velocity.y * dt * 0.5

            # Infinite Wrapping: If a star drifts off the screen grid, teleport it to the other side
            if star_x < 0:
                star_x = SCREEN_WIDTH
            elif star_x > SCREEN_WIDTH:
                star_x = 0
                
            if star_y < 0:
                star_y = SCREEN_HEIGHT
            elif star_y > SCREEN_HEIGHT:
                star_y = 0

            stars[i] = (star_x, star_y)
            pygame.draw.circle(screen, "white", (int(star_x), int(star_y)), 1)

        if screen_shake_time > 0:
            screen_shake_time -= dt

        shake_x = 0
        shake_y = 0
        if screen_shake_time > 0:
            shake_x = random.randint(-6, 6)
            shake_y = random.randint(-6, 6)

        score_surface = score_font.render(f"Score: {score}", True, "white")
        screen.blit(score_surface, (20 + shake_x, 20 + shake_y))

        lives_surface = score_font.render(f"Lives: {lives}", True, "white")
        screen.blit(lives_surface, (20 + shake_x, 80 + shake_y))

        high_score_surface = score_font.render(f"HI: {high_score}", True, "white")
        high_score_x = SCREEN_WIDTH - high_score_surface.get_width() - 20
        screen.blit(high_score_surface, (high_score_x + shake_x, 20 + shake_y))

        for obj in drawable:
            obj.position.x += shake_x
            obj.position.y += shake_y

            obj.draw(screen)

            obj.position.x -= shake_x
            obj.position.y -= shake_y

        # SCREEN DAMAGE FLASH OVERLAY
        if damage_flash_time > 0:
            damage_flash_time -= dt
            flash_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            flash_surf.fill((255, 0, 0))
            flash_surf.set_alpha(100) 
            screen.blit(flash_surf, (0, 0))

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
