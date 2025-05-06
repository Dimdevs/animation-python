import pygame
import os

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Primitive")
clock = pygame.time.Clock()

# Memuat gambar latar belakang dari folder 'assets'
background_morning = pygame.image.load(os.path.join(os.path.dirname(__file__), 'assets', "background-morning.png"))
background_afternoon = pygame.image.load(os.path.join(os.path.dirname(__file__), 'assets', "background-afternoon.png"))

# Mengubah ukuran latar belakang agar sesuai dengan layar
background_morning = pygame.transform.scale(background_morning, (800, 600))
background_afternoon = pygame.transform.scale(background_afternoon, (800, 600))

# Memuat gambar karakter (manusia, herbivora, karnivora)
human_image = pygame.image.load(os.path.join(os.path.dirname(__file__), 'assets', "human.png"))
herbivore_image = pygame.image.load(os.path.join(os.path.dirname(__file__), 'assets', "herbivore.png"))
carnivore_image = pygame.image.load(os.path.join(os.path.dirname(__file__), 'assets', "carnivore.png"))

# Posisi awal karakter (Herbivore, Carnivore, Human)
herbivore_pos = [1000, 350]  # Herbivore starts on the far right
carnivore_pos = [850, 375]   # Carnivore starts slightly to the left of the herbivore (adjusted y-position)
human_pos = [750, 400]       # Human starts to the left of the carnivore (adjusted y-position)

# Kecepatan pergerakan karakter
human_speed = 2
herbivore_speed = 2
carnivore_speed = 2

# Status permainan
running = True
start_time = pygame.time.get_ticks()  # Waktu mulai program
bg_change_delay = 3000  # Waktu dalam milidetik untuk perubahan latar belakang (3 detik)
bg_state = "morning"  # Status latar belakang

while running:
    current_time = pygame.time.get_ticks()  # Waktu saat ini

    # Mengganti latar belakang setelah beberapa detik dan berulang
    if current_time - start_time >= bg_change_delay:
        if bg_state == "morning":
            bg_state = "afternoon"
        else:
            bg_state = "morning"
        
        start_time = current_time  # Reset waktu mulai untuk interval berikutnya

    # Memilih latar belakang sesuai dengan waktu
    if bg_state == "morning":
        screen.blit(background_morning, (0, 0))
    else:
        screen.blit(background_afternoon, (0, 0))

    # Menggerakkan karakter:
    # Herbivora bergerak ke kiri
    herbivore_pos[0] -= herbivore_speed

    # Karnivora mengejar herbivora
    if carnivore_pos[0] > herbivore_pos[0]:
        carnivore_pos[0] -= carnivore_speed  # Ke kiri untuk mengejar herbivora
    else:
        carnivore_pos[0] += carnivore_speed  # Ke kanan jika sudah lewat

    # Manusia mengejar karnivora
    if human_pos[0] > carnivore_pos[0]:
        human_pos[0] -= human_speed  # Ke kiri untuk mengejar karnivora
    else:
        human_pos[0] += human_speed  # Ke kanan jika sudah lewat

    # Reset posisi karakter ketika keluar dari layar (looping efek)
    if herbivore_pos[0] < -100:
        herbivore_pos[0] = 1000  # Reset herbivore to the far right
    if carnivore_pos[0] < -100:
        carnivore_pos[0] = 1000  # Reset carnivore to the right of herbivore
    if human_pos[0] < -100:
        human_pos[0] = 1000  # Reset human to the left of carnivore

    # Menggambar karakter
    screen.blit(human_image, human_pos)
    screen.blit(herbivore_image, herbivore_pos)
    screen.blit(carnivore_image, carnivore_pos)

    pygame.display.flip()  # Update tampilan
    clock.tick(60)  # Kecepatan frame

    # Mengecek apakah jendela ditutup
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
