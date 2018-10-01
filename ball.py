import pygame
from pygame.sprite import Sprite
from settings import Settings


class Ball(Sprite):
    """Class representing pong ball"""
    def __init__(self, screen):
        super(Ball, self).__init__()
        self.screen = screen

        # load up settings
        self.settings = Settings

        # loads ball image
        self.image = pygame.image.load('images/ball.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # saves location for center of screen
        self.rect.centery = self.screen_rect.centery
        self.rect.centerx = self.screen_rect.centerx
        self.centery = float(self.rect.centery)
        self.centerx = float(self.rect.centerx)

        # initialize movement flags
        self.moving_right = self.moving_left = self.moving_down = False
        self.moving_up = True

        # initialize to zero
        self.oldy = 0
        self.oldx = 0

    def blitme(self):
        """Draw ball at current location"""
        self.screen.blit(self.image, self.rect)

    def update(self, score, paddle_ml, paddle_mr, paddle_tl, paddle_bl, paddle_tr, paddle_br):
        ball = self.rect

        # ball going up
        if self.moving_up:
            self.centery -= self.settings.ball_speed
            # ball going right
            if self.oldx < self.centerx:
                self.oldy = self.centery
                self.oldx = self.centerx
                self.centerx += self.settings.ball_speed
                self.moving_left = False
                self.moving_right = True
            # ball going left
            elif self.oldx > self.centerx:
                self.oldy = self.centery
                self.oldx = self.centerx
                self.centerx -= self.settings.ball_speed
                self.moving_left = True
                self.moving_right = False
            # ball collides with one of the top paddles
            if ball.colliderect(paddle_tl) or ball.colliderect(paddle_tr):
                pygame.mixer.music.play()
                self.moving_down = True
                self.moving_up = False
            # computer right paddle
            if ball.colliderect(paddle_mr.rect):
                pygame.mixer.music.play()
                self.centery += 1
                self.moving_right = False
                self.moving_left = True
                self.centerx += -self.settings.ball_speed
                # speed up ball after each strike
                self.settings.ball_speed += self.settings.ball_speedup
            # player left paddle
            if ball.colliderect(paddle_ml.rect):
                pygame.mixer.music.play()
                self.centery += 1
                self.moving_right = True
                self.moving_left = False
                self.centerx += self.settings.ball_speed
                # speed up ball after each strike
                self.settings.ball_speed += self.settings.ball_speedup

        # IF - ball moving down
        if self.moving_down:
            self.centery += self.settings.ball_speed
            # ball moving down in the right direction
            if self.oldx < self.centerx:
                self.moving_right = True
                self.moving_left = False
                self.oldx = self.centerx
                self.centerx += self.settings.ball_speed
            # ball moving down in the left direction
            elif self.oldx > self.centerx:
                self.moving_right = False
                self.moving_left = True
                self.oldx = self.centerx
                self.oldy = self.centery
                self.centerx -= self.settings.ball_speed
            # if ball hits bottom paddle bounce off
            if ball.colliderect(paddle_bl) or ball.colliderect(paddle_br):
                self.moving_down = False
                self.moving_up = True
                pygame.mixer.music.play()
            # player 2 right side paddle
            if ball.colliderect(paddle_mr.rect):
                pygame.mixer.music.play()
                self.centery += 2.5
                self.moving_right = False
                self.moving_left = True
                self.centerx += -self.settings.ball_speed
                # speed up the ball after each paddle strikes
                self.settings.ball_speed += self.settings.ball_speedup
            # player 1
            if ball.colliderect(paddle_ml.rect):
                pygame.mixer.music.play()
                self.centery += 1
                self.moving_right = True
                self.moving_left = False
                self.centerx += self.settings.ball_speed
                # speed up ball after each strike
                self.settings.ball_speed += self.settings.ball_speedup

        # IF - ball out of bounds
        if ball.top > self.screen_rect.bottom or ball.bottom < self.screen_rect.top \
                or ball.left > self.screen_rect.right or ball.right < self.screen_rect.left:
            # IF - what side it went out of bounds
            if ball.centerx > self.screen_rect.centerx:
                score.player2_score += 1
            elif ball.centerx < self.screen_rect.centerx:
                score.player1_score += 1

            score.prep_score()
            self.rect.centery = self.screen_rect.centery
            self.rect.centerx = self.screen_rect.centerx
            self.centery = float(self.rect.centery)
            self.centerx = float(self.rect.centerx)

            # reset ball speed
            self.settings.ball_speed = 0.3

        # new ball position
        self.rect.centery = self.centery
        self.rect.centerx = self.centerx

