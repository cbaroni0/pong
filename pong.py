import pygame
from settings import Settings
from scoreboard import Scoreboard
from button import Button
from ball import Ball
from paddle import Paddle
import game_functions as gf


def run_game():
    pygame.init()
    pygame.mixer.music.load('sound/hitsound.wav')
    pygame.display.set_caption("Pong")
    setting = Settings()

    # Create window
    setting.game_active = False
    window = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    screen_rect = window.get_rect()
    window.fill((255, 255, 255))

    # make the play button
    play = Button(window, "Play")
    font = pygame.font.SysFont(None, 75)
    font_color = (255, 255, 255)
    button_color = (255, 255, 255)
    center = screen_rect.center
    message = font.render("", True, font_color, button_color)
    button_rect = message.get_rect()
    button_rect.center = center
    # ml 1 mr 2 tl 3 bl 4 tr 5 br 6
    paddle_ml = Paddle(window, 1)
    paddle_mr = Paddle(window, 2)
    paddle_tl = Paddle(window, 3)
    paddle_bl = Paddle(window, 4)
    paddle_tr = Paddle(window, 5)
    paddle_br = Paddle(window, 6)
    ball = Ball(window)
    score = Scoreboard(window)

    # Main game loop
    while True:
        gf.check_events(ball, play, setting,
                        paddle_ml, paddle_mr, paddle_tl, paddle_bl, paddle_tr, paddle_br)
        if setting.game_active:
            ball.update(score, paddle_ml, paddle_mr, paddle_tl, paddle_bl, paddle_tr, paddle_br)
            paddle_ml.update()
            paddle_mr.update()
            paddle_tl.update()
            paddle_bl.update()
            paddle_tr.update()
            paddle_br.update()

        window.blit(message, button_rect)
        gf.update_screen(ball, window, score, play, setting,
                         paddle_ml, paddle_mr, paddle_tl, paddle_bl, paddle_tr, paddle_br)


run_game()
