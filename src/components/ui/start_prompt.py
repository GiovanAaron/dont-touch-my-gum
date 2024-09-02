import pygame
from game_context import GameContext

class StartPrompt(pygame.sprite.Sprite):
    def __init__(self):
        self.start_prompt = pygame.image.load("data/assets/start_prompt.png").convert_alpha()
        self.start_prompt_rect = self.start_prompt.get_rect()
        self.start_prompt_rect.center = (GameContext.WIDTH/2, 250)


        self.transparency = 0
        self.start_prompt.set_alpha(self.transparency)
        self.visible = False
        
        self.timer = 0


    
    def update(self):

        if self.transparency >= 225:
            self.visible = True
        if self.transparency <= 0:
            self.visible = False


        self.timer += 1
        if self.timer % 1 == 0:
            
            if self.visible == False:
                self.transparency += 4
            if self.visible == True:
                self.transparency -= 2
        
        self.start_prompt.set_alpha(self.transparency)

        

        
    def draw(self, screen):

        screen.blit(self.start_prompt, self.start_prompt_rect)

            

        



        




        