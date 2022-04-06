class GameStats():
    """Отслеживание статистики для игры AlienInvasion"""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        # Игра начинается с флагом True и заканчивается когда
        # количество жизней будет меньше, чем ship_limit,  флаг становится False
        self.game_active = False   # вот почему черный экран сука был
        self.high_score = 0

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры """
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1