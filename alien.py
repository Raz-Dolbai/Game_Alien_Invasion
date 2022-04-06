import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс представляющий одного прищельца"""

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # загрузка изображения пришельца
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # каждый новый пришелец появляется в левом верхнем углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # сохранение точной позиции пришельца
        self.x = float(self.rect.x)

    def blitme(self):
        """Выводит пришельца в текущем положении"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Перемещает пришельцф вправо """
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edge(self):
        """Возвращает True если пришелец достиг краев экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
