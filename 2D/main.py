import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ping Pong Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

ball_speed_x = 7
ball_speed_y = 7
paddle_speed = 10

paddle_width = 15
paddle_height = 100
player_x = 50
player_y = (screen_height - paddle_height) // 2
opponent_x = screen_width - paddle_width - 50
opponent_y = (screen_height - paddle_height) // 2

ball_width = 20
ball_x = screen_width // 2 - ball_width // 2
ball_y = screen_height // 2 - ball_width // 2

player_score = 0
opponent_score = 0

def draw_objects():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player_x, player_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (opponent_x, opponent_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, ball_width, ball_width))
    pygame.draw.aaline(screen, WHITE, (screen_width // 2, 0), (screen_width // 2, screen_height))
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"{player_score} - {opponent_score}", True, WHITE)
    screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, 20))

def update_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y, player_score, opponent_score
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    if ball_y <= 0 or ball_y >= screen_height - ball_width:
        ball_speed_y *= -1
    if ball_x <= player_x + paddle_width and player_y <= ball_y + ball_width <= player_y + paddle_height:
        ball_speed_x *= -1
        ball_speed_y += random.choice([-1, 1])
    if ball_x >= opponent_x - ball_width and opponent_y <= ball_y + ball_width <= opponent_y + paddle_height:
        ball_speed_x *= -1
        ball_speed_y += random.choice([-1, 1])
    if ball_x <= 0:
        opponent_score += 1
        reset_ball()
    elif ball_x >= screen_width:
        player_score += 1
        reset_ball()

def reset_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    ball_x = screen_width // 2 - ball_width // 2
    ball_y = screen_height // 2 - ball_width // 2
    ball_speed_x *= random.choice([1, -1])
    ball_speed_y *= random.choice([1, -1])

def move_paddle_player():
    global player_y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_y > 0:
        player_y -= paddle_speed
    if keys[pygame.K_s] and player_y < screen_height - paddle_height:
        player_y += paddle_speed

# Fungsi untuk menggerakkan paddle lawan (AI)
def move_paddle_opponent():
    global opponent_y
    if opponent_y + paddle_height / 2 < ball_y + ball_width / 2:
        opponent_y += paddle_speed
    elif opponent_y + paddle_height / 2 > ball_y + ball_width / 2:
        opponent_y -= paddle_speed
    opponent_y = max(0, min(screen_height - paddle_height, opponent_y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    move_paddle_player()
    move_paddle_opponent()
    update_ball()
    draw_objects()
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()
