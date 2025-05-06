import pygame
import random
import os

class Herbivore:
    def __init__(self):
        self.x = random.randint(50, 750)
        self.y = random.randint(50, 550)
        image_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'herbivore.png')
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
