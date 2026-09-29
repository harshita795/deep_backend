import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_ACCELERATION, PLAYER_FRICTION, SCREEN_WIDTH, SCREEN_HEIGHT, INVINCIBILITY_DURATION_SECONDS
from shot import Shot

class Player(CircleShape):
    def __init__(self, x: float ,y: float) -> None: 
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0.0
        self.velocity = pygame.Vector2(0, 0)
        self.invincible_timer = 0.0

    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

        if self.invincible_timer > 0:
            pygame.draw.circle(screen, "white", self.position, self.radius + 10, 1)

    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        if self.invincible_timer > 0:
            self.invincible_timer -= dt

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= dt
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.velocity *= PLAYER_FRICTION

        self.position += self.velocity * dt

        self.wrap_around()

    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        self.velocity += rotated_vector * PLAYER_ACCELERATION * dt

    def shoot(self, force: bool = False) -> None:
        # Only block the shot if we aren't forcing a manual click!
        if not force and self.shoot_cooldown > 0:
            return

        shot = Shot(self.position.x, self.position.y)
        direction = pygame.Vector2(0, 1)
        direction = direction.rotate(self.rotation)
        shot.velocity = direction * PLAYER_SHOOT_SPEED

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT]:
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS / 2
        else: 
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS

    def respawn(self) -> None:
        # Overwrite the position coordinates to the exact center of the screen grid
        self.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        # Reset the physics velocity to zero so the ship isn't drifting anymore
        self.velocity = pygame.Vector2(0, 0)
        self.invincible_timer = INVINCIBILITY_DURATION_SECONDS
