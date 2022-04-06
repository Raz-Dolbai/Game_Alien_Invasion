import sys

import pygame

from settings import Settings

from game_stats import GameStats

from ship import Ship

from pygame.sprite import Group

from alien import Alien

import game_function as gf

from button import Button

from scoreboard import Scoreboard


def run_game():
    pygame.init()  # инициализирует pygame
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_widht, ai_settings.screen_height))  # устанавливает размер экрана
    pygame.display.set_caption('Alien Invasion')  # устанвливает имя окна
    play_button = Button(ai_settings, screen, "Play")
    ship = Ship(ai_settings, screen)  # создаем корабль
    bullets = Group()  # груп из объекта sprite работает с группой объектов
    aliens = Group()  # создание группы кораблей
    alien = Alien(ai_settings, screen)  # создаем пришельца
    gf.create_fleet(ai_settings, screen, ship, aliens)  # содание флота пришельцев
    # создание экземпляра для хранения игровой статистики
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            play_button.draw_button()
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb,  ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
