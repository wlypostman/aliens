import pygame
from bullet import Bullet
from alien import Alien
'''功能'''


def update_screen(screen, ai_settings, ship, bullets, aliens):
    '''更新屏幕'''
    screen.fill(ai_settings.bg_color)
    ship.blit_me()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    aliens.draw(screen)
    pygame.display.flip()


def check_event(ship, screen, ai_settings, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ship, screen, ai_settings, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)
        elif event.type == pygame.K_q:
            exit()


def check_keydown_event(event, ship, screen, ai_settings, bullets):
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(screen, ship, ai_settings, bullets)


def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False


def fire_bullet(screen, ship, ai_settings, bullets):
    if len(bullets) < ai_settings.bullet_allow:
        newbullet = Bullet(screen, ship, ai_settings)
        bullets.add(newbullet)


def update_bullet(bullets):
    for bullet in bullets.copy():
        if bullet.rect.y <= 0:
            bullets.remove(bullet)


def create_fleet(ai_settings, screen, aliens):
    number_x = get_number_x(ai_settings, screen)   
    for number  in range(number_x):
        create_alien(ai_settings,screen, aliens, number)


def get_number_x(ai_settings, screen):
    alien = Alien(screen, ai_settings)
    alien_width = alien.rect.width
    space_x = ai_settings.screen_width - (2 * alien_width)
    number_x = int(space_x / (2 * alien_width))
    return number_x

def create_alien(ai_settings,screen, aliens, number):
    alien = Alien(screen, ai_settings)
    alien_width = alien.rect.width
    alien.rect.x = alien_width + 2 * alien_width * number
    aliens.add(alien)
