import pygame
import sys


def check_events(ball, play, setting, paddle1, paddle2, paddle3, paddle4, paddle5, paddle6):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            check_key_down_events(event, paddle2, paddle5, paddle6)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, paddle2, paddle5, paddle6)
        elif event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(play, mouse_x, mouse_y, setting)

    ball = ball.rect

    # Sets movement direction flags
    if paddle1.rect.bottom < ball.centery:
        paddle1.moving_down = True
        paddle1.moving_up = False

    if paddle1.rect.top > ball.centery:
        paddle1.moving_up = True
        paddle1.moving_down = False

    if paddle3.rect.left > ball.centerx:
        paddle3.moving_left = True
        paddle3.moving_right = False

    if paddle3.rect.right < ball.centerx:
        paddle3.moving_right = True
        paddle3.moving_left = False

    if paddle4.rect.left > ball.centerx:
        paddle4.moving_left = True
        paddle4.moving_right = False

    if paddle4.rect.right < ball.centerx:
        paddle4.moving_right = True
        paddle4.moving_left = False


def check_play_button(play, mouse_x, mouse_y, setting):
    button_clicked = play.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not setting.game_active:
        setting.game_active = True


def update_screen(ball, window, score, play, setting, paddle1, paddle2, paddle3, paddle4, paddle5, paddle6):
    window.fill((255, 255, 255))
    paddle1.blitme()
    paddle2.blitme()
    paddle3.blitme()
    paddle4.blitme()
    paddle5.blitme()
    paddle6.blitme()
    ball.blitme()
    score.show_score()
    if not setting.game_active:
        play.draw_button()
    pygame.display.flip()


def check_key_down_events(event, paddle2, paddle5, paddle6):
    if event.key == pygame.K_UP:
        paddle2.moving_up = True
    elif event.key == pygame.K_DOWN:
        paddle2.moving_down = True
    elif event.key == pygame.K_RIGHT:
        paddle5.moving_right = True
        paddle6.moving_right = True
    elif event.key == pygame.K_LEFT:
        paddle5.moving_left = True
        paddle6.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_key_up_events(event, paddle2, paddle5, paddle6):
    if event.key == pygame.K_UP:
        paddle2.moving_up = False
    elif event.key == pygame.K_DOWN:
        paddle2.moving_down = False
    elif event.key == pygame.K_RIGHT:
        paddle5.moving_right = False
        paddle6.moving_right = False
    elif event.key == pygame.K_LEFT:
        paddle5.moving_left = False
        paddle6.moving_left = False
