import pygame
from game_context import GameContext
from play_status import PlayStatus




class Credits:
    def __init__(self):
       
        # Ensure the screen is set up before accessing it
        GameContext.build_screen()
        self.screen = GameContext.SCREEN
        self.timer = 0

        # Load images and set up background
        self.bg = pygame.Surface(self.screen.get_size())
        self.bg.fill((255, 255, 255))
        
        # Load images with proper method call
        self.personal_logo = pygame.image.load("data/assets/ui/giovan_aaron.png").convert_alpha()
        self.personal_caption = pygame.image.load("data/assets/ui/caption.png").convert_alpha()
        self.DTMG_logo = pygame.image.load("data/assets/ui/logo.png")

        self.personal_logo_rect = self.personal_logo.get_rect()
        self.personal_logo_rect.center = (GameContext.WIDTH/2, GameContext.HEIGHT/2)
        
        self.DTMG_logo_rect = self.DTMG_logo.get_rect()
        self.DTMG_logo_rect.center = (GameContext.WIDTH/2, 100)

        self.personal_caption_rect = self.personal_caption.get_rect()
        self.personal_caption_rect.center = (GameContext.WIDTH/2, 600)

    def update(self):
        self.timer += 1/60
        
        if self.timer >= 3:
            GameContext.PLAY_STATE = PlayStatus.MAIN_MENU

        

    def draw(self):
        # Method to draw on the screen
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.personal_logo, self.personal_logo_rect)  # Adjust position as needed
        self.screen.blit(self.personal_caption, self.personal_caption_rect)  # Adjust position as needed
        self.screen.blit(self.DTMG_logo, self.DTMG_logo_rect)  # Adjust position as needed
