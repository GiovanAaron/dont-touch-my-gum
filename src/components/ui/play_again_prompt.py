import pygame
from game_context import GameContext

class PlayAgainPrompt(pygame.sprite.Sprite):
    def __init__(self):
        self.prompt = pygame.image.load("data/assets/play_again_prompt.png").convert_alpha()
        self.prompt_rect = self.prompt.get_rect()
        self.prompt_rect.center = (GameContext.WIDTH/2, GameContext.HEIGHT - 100)


        self.transparency = 0
        self.prompt.set_alpha(self.transparency)
        self.visible = False
        
        self.timer = 0


    
    def update(self):
        

        if self.transparency >= 225:
            self.visible = True
        if self.transparency <= 0:
            self.visible = False


        self.timer += 1
        if self.timer >= 60 * 1.5:
            if self.timer % 1 == 0:
                
                if self.visible == False:
                    self.transparency += 4
                if self.visible == True:
                    self.transparency -= 2
            
            self.prompt.set_alpha(self.transparency)

        

        
    def draw(self, screen):

        screen.blit(self.prompt, self.prompt_rect)

            

        



        




        