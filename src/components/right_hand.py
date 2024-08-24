import pygame
import math

class RightHand(pygame.sprite.Sprite):
    def __init__ (self, position):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("data/assets/enemy_right_hand.png")
        self.rect = self.image.get_rect(center=position)
        self.speed = 1

    def update(self)
        

   
