import pygame
from game_context import GameContext

class HighestScore(pygame.sprite.Sprite): 
    def __init__(self, height=165):

        
        self.font = pygame.font.Font("data/fonts/OpenSans-SemiboldItalic.ttf", 16)
        self.score = self.font.render(f"Best Score: {GameContext.HIGHEST_SCORE}", True, "#00B0E9")
        self.score.set_alpha(200)
        self.rect = self.score.get_rect()
        self.rect.center = (GameContext.WIDTH/2, height)


    def draw(self, screen):

        screen.blit(self.score, self.rect)
        
        

