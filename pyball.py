import pygame
import random
import sys

# Initialize
pygame.init()

WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pickleball")

clock = pygame.time.Clock()

# Colors
WHITE = (245, 245, 245)
GREEN = (30, 130, 76)
YELLOW = (235, 220, 70)
BLACK = (20, 20, 20)

# Paddle settings
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 110
PADDLE_SPEED = 7

left = pygame.Rect(40, HEIGHT//2 - PADDLE_HEIGHT//2,
                   PADDLE_WIDTH, PADDLE_HEIGHT)
right = pygame.Rect(WIDTH-55, HEIGHT//2 - PADDLE_HEIGHT//2,
                    PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball
BALL_RADIUS = 12
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed = 7
ball_dx = random.choice([-1, 1]) * ball_speed
ball_dy = random.choice([-4, -3, 3, 4])

# Score
left_score = 0
right_score = 0

font = pygame.font.SysFont(None, 48)


def reset_ball():
    global ball_x, ball_y, ball_dx, ball_dy
    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2
    ball_dx = random.choice([-1, 1]) * ball_speed
    ball_dy = random.choice([-4, -3, 3, 4])


running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and left.top > 0:
        left.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left.bottom < HEIGHT:
        left.y += PADDLE_SPEED

    if keys[pygame.K_UP] and right.top > 0:
        right.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right.bottom < HEIGHT:
        right.y += PADDLE_SPEED

    # Ball movement
    ball_x += ball_dx
    ball_y += ball_dy

    # Top/bottom bounce
    if ball_y - BALL_RADIUS <= 0 or ball_y + BALL_RADIUS >= HEIGHT:
        ball_dy *= -1

    # Ball rectangle for collision
    ball_rect = pygame.Rect(
        ball_x - BALL_RADIUS,
        ball_y - BALL_RADIUS,
        BALL_RADIUS * 2,
        BALL_RADIUS * 2
    )

    # Paddle collisions
    if ball_rect.colliderect(left) and ball_dx < 0:
        ball_dx *= -1.05
        ball_dy *= 1.05

    if ball_rect.colliderect(right) and ball_dx > 0:
        ball_dx *= -1.05
        ball_dy *= 1.05

    # Scoring
    if ball_x < 0:
        right_score += 1
        reset_ball()

    if ball_x > WIDTH:
        left_score += 1
        reset_ball()

    # Draw court
    screen.fill(GREEN)

    pygame.draw.line(screen, WHITE,
                     (WIDTH//2, 0),
                     (WIDTH//2, HEIGHT), 4)

    # Draw paddles
    pygame.draw.rect(screen, WHITE, left)
    pygame.draw.rect(screen, WHITE, right)

    # Draw pickleball
    pygame.draw.circle(screen, YELLOW,
                       (int(ball_x), int(ball_y)),
                       BALL_RADIUS)

    # Holes in pickleball
    holes = [
        (-5,-5),(0,-6),(5,-5),
        (-6,0),(0,0),(6,0),
        (-5,5),(0,6),(5,5)
    ]

    for dx, dy in holes:
        pygame.draw.circle(
            screen,
            BLACK,
            (int(ball_x + dx), int(ball_y + dy)),
            2
        )

    # Scores
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)

    screen.blit(left_text, (WIDTH//2 - 80, 20))
    screen.blit(right_text, (WIDTH//2 + 50, 20))

    pygame.display.flip()

pygame.quit()
sys.exit()