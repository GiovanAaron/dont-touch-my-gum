import pygame
from game_context import GameContext
from play_status import PlayStatus



class MainMenu:
    def __init__(self):

        GameContext.build_screen()
        self.screen = GameContext.SCREEN

        self.DTMG_logo = pygame.image.load("data/assets/logo.png")
        self.DTMG_logo_rect = self.DTMG_logo.get_rect()
        self.DTMG_logo_rect.center = (GameContext.WIDTH/2, 100)
        self.background = pygame.image.load('./data/assets/background.png').convert_alpha()

        self.start_prompt = pygame.image.load("data/assets/start_prompt.png").convert_alpha()
        self.start_prompt_rect = self.start_prompt.get_rect()
        self.start_prompt_rect.center = (GameContext.WIDTH/2, 250)


        self.mascot = pygame.image.load("data/assets/mascot.png").convert_alpha()
        self.mascot_rect = self.mascot.get_rect()
        self.mascot_rect.center = (GameContext.WIDTH/2, 350)

        self.display_hands = pygame.image.load("data/assets/display_hands.png").convert_alpha()
        self.display_hands_rect = self.display_hands.get_rect()
        self.display_hands_rect.center = (GameContext.WIDTH/2, 429 + 211 / 2)


    def update(self, keys):
       
        if any(keys):  # Check if the SPACE key is pressed
            GameContext.PLAY_STATE = PlayStatus.GAMEPLAY
        

    


    def draw(self):
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.DTMG_logo, self.DTMG_logo_rect)
        self.screen.blit(self.start_prompt, self.start_prompt_rect)
        self.screen.blit(self.mascot, self.mascot_rect)
        self.screen.blit(self.display_hands, self.display_hands_rect)

    