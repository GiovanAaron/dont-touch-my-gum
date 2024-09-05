import pygame
from game_context import GameContext

class YellowSpark(pygame.sprite.Sprite):
    def __init__(self):

        self.image = pygame.image.load("data/assets/ui/yellow_spark_1.png").convert_alpha()
        self.image2 = pygame.image.load("data/assets/ui/yellow_spark_2.png").convert_alpha()
        
        self.rect = self.image.get_rect()
        self.rect2 = self.image2.get_rect()

        self.rect.center = (GameContext.WIDTH/2, 325)
        

        self.state = True

        self.timer = 0
    
    def update(self):
        
        self.timer += 1

        if self.timer % 120 == 0:
            self.state = not self.state


    def draw(self, screen):

        if self.state:
            screen.blit(self.image, self.rect)
        else: screen.blit(self.image2, self.rect)
        

