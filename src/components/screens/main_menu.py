import pygame
from game_context import GameContext
from play_status import PlayStatus
from src.components.ui.start_prompt import StartPrompt
from src.components.ui.highest_score import HighestScore
from src.components.ui.mascot import Mascot
from src.components.ui.yellow_spark import YellowSpark
from src.components.ui.white_sparkle import WhiteSparkle



class MainMenu:
    def __init__(self):

        # GameContext.build_screen()
        self.screen = GameContext.SCREEN
        self.start_time = pygame.time.get_ticks()

        

        self.DTMG_logo = pygame.image.load("data/assets/ui/logo_without_shine.png")
        self.DTMG_logo_rect = self.DTMG_logo.get_rect()
        self.DTMG_logo_rect.center = (GameContext.WIDTH/2 +6, 100)
        self.background = pygame.image.load('./data/assets/background.png').convert_alpha()
        self.yellow_spark = YellowSpark()
        self.white_sparkle = WhiteSparkle()


        # self.start_prompt = pygame.image.load("data/assets/start_prompt.png").convert_alpha()
        # self.start_prompt_rect = self.start_prompt.get_rect()
        # self.start_prompt_rect.center = (GameContext.WIDTH/2, 250)


        # animated prompt
        self.start_prompt = StartPrompt()

        # highest score
        self.score = HighestScore()
        

        

        self.display_hands = pygame.image.load("data/assets/display_hands.png").convert_alpha()
        self.display_hands_rect = self.display_hands.get_rect()
        self.display_hands_rect.center = (GameContext.WIDTH/2, 429 + 211 / 2)

        self.mascot = Mascot()

        self.sparkle_cluster = pygame.sprite.Group(
            WhiteSparkle((79 + 5 ,43), 150),
            WhiteSparkle((72 + 5,61), 550),
            WhiteSparkle((90 + 5,59), 950)
        )


    def update(self, keys):
       
        self.yellow_spark.update()
        self.start_prompt.update()
        self.current_time = pygame.time.get_ticks()

        # Check if 3 seconds have passed
        if self.current_time - self.start_time >= 2000:  
            if any(keys):  # Check if any key is pressed
                GameContext.PLAY_STATE = PlayStatus.TUTORIAL
        
        
        
        self.mascot.update()
        self.white_sparkle.update()

        self.sparkle_cluster.update()

    def draw(self):
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.DTMG_logo, self.DTMG_logo_rect)
        
        
        self.screen.blit(self.display_hands, self.display_hands_rect)
        
        self.start_prompt.draw(self.screen)
        
        self.score.draw(self.screen)

        self.mascot.draw(self.screen)

        self.yellow_spark.draw(self.screen)

        # self.white_sparkle.draw(self.screen)

        self.sparkle_cluster.draw(self.screen)
        
        
    