import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, screen, ai_settings):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        self.image = pygame.image.load('images/1.png')        
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blit_me(self):
        self.screen(self.image, self.rect)

    def update(self):
        self.x -= self.ai_settings.alien_speed_factor
        self.rect.x = self.x