import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Senja dengan Mobil Berjalan")

# Warna
SKY_TOP = (255, 153, 102)
SKY_BOTTOM = (51, 102, 255)
MOUNTAIN = (34, 32, 52)
GROUND = (102, 51, 0)
CAR_BODY = (255, 0, 0)
WHEEL = (0, 0, 0)
WINDOW = (173, 216, 230)
TREE_TRUNK = (101, 67, 33)
TREE_LEAF = (0, 100, 0)
BIRD = (0, 0, 0)

# Clock
clock = pygame.time.Clock()

# Posisi mobil
car_x = 0

# Fungsi gambar mobil
def draw_car(x):
    pygame.draw.rect(screen, CAR_BODY, (x, 250, 100, 40))           # badan mobil
    pygame.draw.circle(screen, WHEEL, (x+20, 290), 10)              # roda depan
    pygame.draw.circle(screen, WHEEL, (x+80, 290), 10)              # roda belakang
    pygame.draw.rect(screen, WINDOW, (x+20, 255, 25, 20))           # jendela depan
    pygame.draw.rect(screen, WINDOW, (x+55, 255, 25, 20))           # jendela belakang

# Fungsi gambar gunung
def draw_mountains():
    pygame.draw.polygon(screen, MOUNTAIN, [(0, 300), (100, 170), (200, 300)])
    pygame.draw.polygon(screen, MOUNTAIN, [(150, 300), (300, 130), (450, 300)])
    pygame.draw.polygon(screen, MOUNTAIN, [(400, 300), (550, 180), (700, 300)])
    pygame.draw.polygon(screen, MOUNTAIN, [(600, 300), (720, 200), (800, 300)])

# Fungsi gambar gradasi langit
def draw_gradient_sky():
    for i in range(HEIGHT // 2):
        r = SKY_TOP[0] + (SKY_BOTTOM[0] - SKY_TOP[0]) * i // (HEIGHT // 2)
        g = SKY_TOP[1] + (SKY_BOTTOM[1] - SKY_TOP[1]) * i // (HEIGHT // 2)
        b = SKY_TOP[2] + (SKY_BOTTOM[2] - SKY_TOP[2]) * i // (HEIGHT // 2)
        pygame.draw.line(screen, (r, g, b), (0, i), (WIDTH, i))

# Fungsi gambar matahari dengan glow
def draw_sun():
    sun = pygame.Surface((120, 120), pygame.SRCALPHA)
    pygame.draw.circle(sun, (255, 200, 0, 150), (60, 60), 40)
    pygame.draw.circle(sun, (255, 200, 0, 50), (60, 60), 60)
    screen.blit(sun, (600, 40))

# Fungsi gambar pohon
def draw_tree(x, y):
    pygame.draw.rect(screen, TREE_TRUNK, (x + 10, y + 20, 10, 30))
    pygame.draw.circle(screen, TREE_LEAF, (x + 15, y + 15), 20)

# Fungsi gambar burung
def draw_bird(x, y):
    pygame.draw.lines(screen, BIRD, False, [(x, y), (x + 5, y - 5), (x + 10, y)], 2)

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    
    draw_gradient_sky()
    draw_sun()
    draw_mountains()
    pygame.draw.rect(screen, GROUND, (0, HEIGHT//2, WIDTH, HEIGHT//2))  # tanah
    
    # Pohon
    draw_tree(100, 400)
    draw_tree(700, 280)

    # Burung
    draw_bird(200, 100)
    draw_bird(220, 110)
    draw_bird(240, 90)

    # Mobil
    draw_car(car_x)
    car_x += 2
    if car_x > WIDTH:
        car_x = -100

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
