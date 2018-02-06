from sys import exit

import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    '''123'''
    # pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.caption)
    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens, ship)

    while True:
        gf.check_event(ship, screen, ai_settings, bullets)
        ship.update()
        bullets.update()
        gf.update_bullet(bullets)
        gf.alien_update(aliens)
        gf.update_screen(screen, ai_settings, ship, bullets, aliens)


run_game()
