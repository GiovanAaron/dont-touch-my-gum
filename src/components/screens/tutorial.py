import pygame
from game_context import GameContext
from play_status import PlayStatus
from src.components.ui.start_prompt import StartPrompt
from src.components.ui.back import Backbutton


class Tutorial:
    def __init__ (self):
        self.screen = GameContext.SCREEN
        self.start_time = pygame.time.get_ticks()


        self.tutorial_img = pygame.image.load("data/assets/tutorial/instructions screen.png")
        self.tutorial_img_rect = self.tutorial_img.get_rect()
        self.tutorial_img_rect.topleft = (0, 0)
        self.start_prompt = StartPrompt()
        self.start_prompt_img = self.start_prompt.start_prompt
        
        self.back_button = Backbutton()
        

    
    def update(self, keys):
        self.current_time = pygame.time.get_ticks()

        if self.current_time - self.start_time >= 3000:
            if any(keys):
                GameContext.PLAY_STATE = PlayStatus.GAMEPLAY

        if self.current_time - self.start_time >= 5000:
            self.start_prompt.update()

        
        
            

        

    
    def draw(self):

        
        self.screen.blit(self.tutorial_img, self.tutorial_img_rect)
        self.screen.blit(self.start_prompt_img, (50, 320))
        self.back_button.draw(self.screen)

        pygame.display.update()        