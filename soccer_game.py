import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Soccer Legends")

WHITE = (255, 255, 255)
GREEN = (30, 140, 30)
BLUE = (50, 100, 255)
RED = (255, 60, 60)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 50)

clock = pygame.time.Clock()

player = pygame.Rect(200, 300, 30, 30)
enemy = pygame.Rect(700, 300, 30, 30)

ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = 0
ball_dy = 0

player_score = 0
enemy_score = 0

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    speed = 5

    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    # Keep player on field
    player.x = max(0, min(WIDTH - player.width, player.x))
    player.y = max(0, min(HEIGHT - player.height, player.y))

    # Enemy AI follows ball
    if enemy.centery < ball_y:
        enemy.y += 3
    if enemy.centery > ball_y:
        enemy.y -= 3

    if enemy.centerx < ball_x:
        enemy.x += 2
    if enemy.centerx > ball_x:
        enemy.x -= 2

    # Kick ball with space
    if keys[pygame.K_SPACE]:
        dist = math.hypot(player.centerx - ball_x,
                          player.centery - ball_y)

        if dist < 60:
            ball_dx = 10
            ball_dy = 0

    # Enemy kicks ball
    dist_enemy = math.hypot(enemy.centerx - ball_x,
                            enemy.centery - ball_y)

    if dist_enemy < 50:
        ball_dx = -8
        ball_dy = 0

    ball_x += ball_dx
    ball_y += ball_dy

    ball_dx *= 0.98
    ball_dy *= 0.98

    # Goal detection
    if ball_x <= 0 and 220 < ball_y < 380:
        enemy_score += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_dx = 0
        ball_dy = 0

    if ball_x >= WIDTH and 220 < ball_y < 380:
        player_score += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_dx = 0
        ball_dy = 0

    screen.fill(GREEN)

    # Center line
    pygame.draw.line(screen, WHITE,
                     (WIDTH // 2, 0),
                     (WIDTH // 2, HEIGHT), 4)

    pygame.draw.circle(screen, WHITE,
                       (WIDTH // 2, HEIGHT // 2),
                       80, 4)

    # Goals
    pygame.draw.rect(screen, WHITE,
                     (0, 220, 20, 160))

    pygame.draw.rect(screen, WHITE,
                     (980, 220, 20, 160))

    # Players
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, RED, enemy)

    # Ball
    pygame.draw.circle(screen, WHITE,
                       (int(ball_x), int(ball_y)), 12)

    score_text = font.render(
        f"{player_score} - {enemy_score}",
        True,
        BLACK
    )

    screen.blit(score_text, (460, 20))

    pygame.display.flip()

pygame.quit()