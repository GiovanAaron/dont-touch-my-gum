import pygame
from game_context import GameContext
from play_status import PlayStatus
from src.utils.quip_gen import quip_gen
from src.utils.studio_audience_gen import studio_audience_sfx
from src.components.ui.play_again_prompt import PlayAgainPrompt
from src.components.ui.main_menu import MainMenuButton
from src.components.ui.tutorial_icon import TutorialIcon



class GameOver():
    def __init__(self, score=0):
        print(f"Game Over! Your score was: {score}")

        # Get score in text
        self.quip = quip_gen(score)

        self.reaction_sfx = studio_audience_sfx(score)

        
        self.screen = GameContext.SCREEN
        self.start_time = pygame.time.get_ticks()

        self.bg = pygame.Surface(self.screen.get_size())
        self.bg.fill((255, 255, 255))
        self.score_intro = pygame.image.load("data/assets/score_intro.png").convert_alpha()
        self.score_font = pygame.font.Font("data/fonts/OpenSans_Condensed-BoldItalic.ttf", 110)
        self.score_num = self.score_font.render(f"{score}", True, "#74A578")
        # self.prompt = pygame.image.load("data/assets/play_again_prompt.png").convert_alpha()
        self.prompt = PlayAgainPrompt()

        pygame.mixer.music.play(0)
        # self.reaction_sfx.play(0)

        # Get coordinates
        self.score_num_rect = self.score_num.get_rect()
        self.score_num_rect.center = (GameContext.WIDTH/2, 300)
        self.score_intro_rect = self.score_intro.get_rect()
        self.score_intro_rect.center = (GameContext.WIDTH/2, 100)
        # self.prompt_rect = self.prompt.get_rect()
        # self.prompt_rect.center = (GameContext.WIDTH/2, GameContext.HEIGHT - 100)
        self.quip_rect = self.quip.get_rect()
        self.quip_rect.center = (GameContext.WIDTH/2, GameContext.HEIGHT - 150)
        self.main_menu_nav = MainMenuButton()
        self.tutorial_icon = TutorialIcon()




    def update(self, keys):
        self.current_time = pygame.time.get_ticks()

        # Check if 3 seconds have passed
        if self.current_time - self.start_time >= 3000:  # 3000 milliseconds = 3 seconds
            if any(keys):  # Check if any key is pressed
                GameContext.PLAY_STATE = PlayStatus.GAMEPLAY


        if self.current_time - self.start_time >= 13000:  # 3000 milliseconds = 3 seconds
            GameContext.PLAY_STATE = PlayStatus.END_CREDITS

        

        

        self.prompt.update()
        
        
        

    def draw(self):
        # Method to draw on the screen
        
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.score_intro, self.score_intro_rect)
        self.screen.blit(self.score_num, self.score_num_rect)
        # self.screen.blit(self.prompt, self.prompt_rect)
        self.screen.blit(self.quip, self.quip_rect)
        self.prompt.draw(self.screen)
        self.main_menu_nav.draw(self.screen)
        self.tutorial_icon.draw(self.screen)

       