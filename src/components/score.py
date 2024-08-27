import pygame

class ScoreCount(pygame.sprite.Sprite)
    def __init__(self):
        self.image = pygame.image.load("data/assets/score_container.png")
        self.rect = self.image.get_rect()
        self.rect.center = (360/2 , 40 )