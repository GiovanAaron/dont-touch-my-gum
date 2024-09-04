import pygame
import math


class WhiteSparkle(pygame.sprite.Sprite):
    def __init__(self, position=(70, 50), offset=0):
        
        super().__init__()
        self.original_image = pygame.image.load("data/assets/ui/white_sparkle.png").convert_alpha() #this is scaled oversize by 2
        self.image = self.original_image
       
        self.size = 0.5
        # self.image = pygame.transform.scale_by(self.image, 0.5 )
        
        self.rect = self.image.get_rect()
        self.rect.center = position

        self.timer = 0
        self.offset = offset       
        
    
    def update(self):
        
        self.timer += 1
        scale_factor = 0.5 + 0.2 * math.sin(0.045 * self.timer + self.offset)
        new_size = (int(self.original_image.get_width() * scale_factor), 
                    int(self.original_image.get_height() * scale_factor))
        self.image = pygame.transform.scale(self.original_image, new_size)
        self.rect = self.image.get_rect(center=self.rect.center)


    def draw(self, screen):

        screen.blit(self.image, self.rect)

