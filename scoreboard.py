import pygame.font


class Scoreboard:

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.font_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 60)

        self.player1_score = 0
        self.player2_score = 0

        self.prep_score()

    def show_score(self):
        self.screen.blit(self.score1, self.score_rect1)
        self.screen.blit(self.score2, self.score_rect2)
        self.screen.blit(self.score_win, self.score_goal)
        
    def prep_score(self):
        """Create scoreboard"""
        str_score1 = "{:,}".format(self.player1_score)
        str_score2 = "{:,}".format(self.player2_score)
        score_goal = "{:,}".format(15)

        self.score1 = self.font.render(str_score1, True, self.font_color, (255, 255, 255))
        self.score2 = self.font.render(str_score2, True, self.font_color, (255, 255, 255))
        self.score_win = self.font.render(score_goal, True, self.font_color, (255, 255, 255))

        self.score_rect1 = self.score1.get_rect()
        self.score_rect2 = self.score2.get_rect()
        self.score_goal = self.score_win.get_rect()

        self.score_rect1.right = self.screen_rect.centerx + 100
        self.score_rect2.left = self.screen_rect.centerx - 100
        self.score_goal.centerx = self.screen_rect.centerx

        self.score_rect1.top = 40
        self.score_rect2.top = 40
        self.score_goal.top = 60
