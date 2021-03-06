import pygame
import game_functions as gf
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from pygame.sprite import Group


def run_game():
    # initialize the game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # create 'Play' button
    play_button = Button(ai_settings, screen, "Play")
    # create an object for infos
    stats = GameStats(ai_settings)
    # create a ship
    ship = Ship(ai_settings, screen)
    # create a group of bullets
    bullets = Group()
    # create a group of aliens
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # start main loop of game
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)


run_game()
