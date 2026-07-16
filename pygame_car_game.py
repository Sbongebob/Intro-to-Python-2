import pygame
import random
import sys

pygame.init()

# Screen
WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Dodge Game")
clock = pygame.time.Clock()

# Colors
GRAY = (60, 60, 60)
GREEN = (30, 150, 30)
WHITE = (255, 255, 255)
RED = (220, 40, 40)
BLUE = (50, 120, 255)
YELLOW = (255, 255, 0)

font = pygame.font.SysFont(None, 40)

# Road
ROAD_WIDTH = 300
ROAD_X = (WIDTH - ROAD_WIDTH) // 2

# Player
car = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 100, 50, 80)
car_speed = 6

# Enemy
enemy = pygame.Rect(random.randint(ROAD_X + 20, ROAD_X + ROAD_WIDTH - 70),
                    -100, 50, 80)
enemy_speed = 6

score = 0

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and car.left > ROAD_X:
        car.x -= car_speed

    if keys[pygame.K_RIGHT] and car.right < ROAD_X + ROAD_WIDTH:
        car.x += car_speed

    # Move enemy
    enemy.y += enemy_speed

    if enemy.top > HEIGHT:
        score += 1
        enemy.y = -100
        enemy.x = random.randint(
            ROAD_X + 20,
            ROAD_X + ROAD_WIDTH - 70
        )
        enemy_speed += 0.2

    # Collision
    if car.colliderect(enemy):
        break

    # Draw
    screen.fill(GREEN)

    # Road
    pygame.draw.rect(screen, GRAY, (ROAD_X, 0, ROAD_WIDTH, HEIGHT))

    # Lane markings
    for y in range(0, HEIGHT, 40):
        pygame.draw.rect(screen, WHITE,
                         (WIDTH//2 - 5, y, 10, 20))

    # Player car
    pygame.draw.rect(screen, BLUE, car)
    pygame.draw.rect(screen, YELLOW,
                     (car.x + 8, car.y + 10, 10, 15))
    pygame.draw.rect(screen, YELLOW,
                     (car.x + 32, car.y + 10, 10, 15))

    # Enemy car
    pygame.draw.rect(screen, RED, enemy)

    # Score
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()

# Game Over screen
screen.fill((20, 20, 20))
game_over = font.render("GAME OVER", True, RED)
score_text = font.render(f"Final Score: {score}", True, WHITE)

screen.blit(game_over, (150, 300))
screen.blit(score_text, (135, 350))
pygame.display.flip()

pygame.time.wait(3000)

pygame.quit()
sys.exit()