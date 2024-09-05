import pygame
from game_context import GameContext

class Paused(pygame.sprite.Sprite):
    def __init__(self):

        self.box = pygame.image.load("data/assets/ui/pause_overlay.png").convert_alpha()
        self.box.set_alpha(30) 
        self.box_rect = self.box.get_rect()
        self.box_rect.center = (GameContext.WIDTH/2, GameContext.HEIGHT/2)

        self.font = pygame.font.Font("data/fonts/open_serif_italic.ttf", 20)
        self.best_score = self.font.render(f"Best Score: {GameContext.HIGHEST_SCORE}", True, "#666666")
        self.best_score_rect = self.best_score.get_rect()
        self.best_score_rect.center = (GameContext.WIDTH/2, 220)

        self.unpause_prompt = self.font.render(f"Press Space to Unpause", True, "#666666")
        self.unpause_prompt_rect = self.unpause_prompt.get_rect()
        self.unpause_prompt_rect.center = (GameContext.WIDTH/2, 410)


    
    def draw(self, screen):
        

        screen.blit(self.box, self.box_rect)
        screen.blit(self.best_score, self.best_score_rect)
        screen.blit(self.unpause_prompt, self.unpause_prompt_rect)