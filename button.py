import pygame.font
from settings import Settings


class Button:

        def __init__(self, screen, msg):
            """Initialize Start Button"""
            self.screen = screen
            self.screen_rect = screen.get_rect()

            # Setup button info
            setting = Settings()
            self.font = pygame.font.SysFont(None, 48)
            self.width = setting.screen_width
            self.height = setting.screen_height
            self.button_color = (0, 0, 0)
            self.font_color = (255, 255, 255)

            # Create button
            self.rect = pygame.Rect(0, 0, self.width, self.height)
            self.rect.center = self.screen_rect.center

            # Preps button msg
            self.message = self.font.render(msg, True, self.font_color, self.button_color)
            self.button_rect = self.message.get_rect()
            self.button_rect.center = self.rect.center

        def draw_button(self):
            self.screen.fill(self.button_color, self.rect)
            self.screen.blit(self.message, self.button_rect)
