import pygame
from src.utils.sine_calculator import sine_calculate


class WhiteSparkle(pygame.sprite.Sprite):
    def __init__(self):
        
        self.image = pygame.image.load("data/assets/ui/white_sparkle.png").convert_alpha() #this is scaled oversize by 2

       

        self.image = pygame.transform.scale_by(self.image, 0.5 )
        self.rect = self.image.get_rect()
        self.rect.center = (150, 150)

        self.timer = 0
        
        
    
    def update(self):

        self.timer += 1
        
        self.image = pygame.transform.scale_by(self.image, sine_calculate(0.5, self.timer, frequency=1))
        
        


    def draw(self, screen):

        screen.blit(self.image, self.rect)

