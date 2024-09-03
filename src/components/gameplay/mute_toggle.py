import pygame
from game_context import GameContext

class MuteButton (pygame.sprite.Sprite):
    def __init__(self):
        self.screen = GameContext.SCREEN

        self.audio_ON = pygame.image.load("data/assets/music/audio_enabled.png").convert_alpha()
        self.audio_OFF = pygame.image.load("data/assets/music/audio_muted.png").convert_alpha()

        self.audio_ON_rect = self.audio_ON.get_rect()
        self.audio_OFF_rect = self.audio_OFF.get_rect()
        
        self.audio_ON_rect.center = (GameContext.WIDTH - 35, 35)

    

    def update(self, mouse_pos):
        # Check if the mouse is clicking within the audio button's rectangle
        if self.audio_ON_rect.collidepoint(mouse_pos):
            # Toggle the audio state
            GameContext.AUDIO = not GameContext.AUDIO
            

    
    def draw(self, surface):
        if GameContext.AUDIO == True:
            surface.blit(self.audio_ON, self.audio_ON_rect)

        if GameContext.AUDIO == False:
            surface.blit(self.audio_OFF, self.audio_ON_rect)
        

