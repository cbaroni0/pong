import pygame
from pygame.sprite import Sprite
from settings import Settings


class Paddle(Sprite):
    """A class to represent our paddles"""

    def __init__(self, screen, paddle):
        """Initialize paddle"""
        super(Paddle, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.paddle = paddle
        self.top_line = (self.screen_rect.centerx, 0)
        self.bottom_line = (self.screen_rect.centerx, self.screen_rect.bottom)

        if paddle == 1 or paddle == 2:
            self.image = pygame.image.load('images/paddle.png')
        else:
            self.image = pygame.image.load('images/paddle2.png')

        self.rect = self.image.get_rect()

        # ml 1 mr 2 tl 3 bl 4 tr 5 br 6
        if paddle == 1:
            self.rect.centerx = self.screen_rect.left + 20
            self.rect.centery = self.screen_rect.centery
        elif paddle == 2:
            self.rect.centerx = self.screen_rect.right - 20
            self.rect.centery = self.screen_rect.centery
        elif paddle == 3:
            self.rect.centerx = self.screen_rect.left + 200
            self.rect.centery = self.screen_rect.top + 20
        elif paddle == 4:
            self.rect.centerx = self.screen_rect.left + 200
            self.rect.centery = self.screen_rect.bottom - 20
        elif paddle == 5:
            self.rect.centerx = self.screen_rect.right - 200
            self.rect.centery = self.screen_rect.top + 20
        elif paddle == 6:
            self.rect.centerx = self.screen_rect.right - 200
            self.rect.centery = self.screen_rect.bottom - 20

        # Store paddle center
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        # Initialize movement flags
        self.oldy = 0
        self.oldx = 0
        self.moving_up = self.moving_down = self.moving_right = self.moving_left = self.moving = False
        self.was_moving = False

        self.settings = Settings

    def blitme(self):
        """Draw our center divider line"""
        pygame.draw.line(self.screen, (0, 0, 0), self.top_line, self.bottom_line, 5)
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Moves Paddles based on button pushes"""
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            if self.paddle == 1 or self.paddle == 3 or self.paddle == 4:
                self.centery += self.settings.computer_speed
            else:
                self.centery += self.settings.paddle_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            if self.paddle == 1 or self.paddle == 3 or self.paddle == 4:
                self.centery -= self.settings.computer_speed
            else:
                self.centery -= self.settings.paddle_speed

        # computer
        if self.paddle == 3 or self.paddle == 4:
            if self.moving_right and self.rect.right < self.screen_rect.centerx:
                self.centerx += self.settings.computer_speed
            elif self.moving_left and self.rect.left > self.screen_rect.left:
                self.centerx -= self.settings.computer_speed
        # player
        if self.paddle == 5 or self.paddle == 6:
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.centerx += self.settings.paddle_speed
            elif self.moving_left and self.rect.left > self.screen_rect.centerx:
                self.centerx -= self.settings.paddle_speed

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
