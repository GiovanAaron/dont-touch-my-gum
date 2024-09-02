import pygame
from game_context import GameContext
from play_status import PlayStatus


class EndCredits:
    def __init__(self):

        self.image = pygame.image.load("data/assets/ui/credits_roll.png")
        self.image_rect = self.image.get_rect()
        self.pos = 1150  #good starting position is 1200
        self.image_rect.center = (GameContext.WIDTH/2, self.pos)
        self.screen = GameContext.SCREEN
        self.bg_color = (102, 102, 102)
        self.clock = pygame.time.Clock()
        self.timer = 0


    def update(self):
        
        if self.pos == -185:
            self.timer += 1


        if self.timer >= 3000:
            GameContext.PLAY_STATE = PlayStatus.MAIN_MENU

        if self.pos > -185:
            self.pos -= 1
            self.image_rect.center = (GameContext.WIDTH/2, self.pos)
            self.clock.tick(60)
        


    def draw(self):

        self.screen.fill(self.bg_color)
        self.screen.blit(self.image, self.image_rect)

        pygame.display.update()

    

