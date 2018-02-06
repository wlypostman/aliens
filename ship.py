import pygame


class Ship():

    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/1231.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.x = float(self.rect.x)
        self.speed = ai_settings.ship_speed
        self.move_right = False
        self.move_left = False

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed
        if self.move_left and self.rect.left > 0 :
            self.x -= self.speed
        self.rect.x = self.x

