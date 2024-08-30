import pygame
from game_context import GameContext
from play_status import PlayStatus
from src.utils.quip_gen import quip_gen



class GameOver():
    def __init__(self, score):
        print(f"Game Over! Your score was: {score}")

        # Get score in text
        self.quip = quip_gen(score)


        # Ensure the screen is set up before accessing it
        GameContext.build_screen()
        self.screen = GameContext.SCREEN
        self.bg = pygame.Surface(self.screen.get_size())
        self.bg.fill((255, 255, 255))
        self.score_intro = pygame.image.load("data/assets/score_intro.png").convert_alpha()
        self.score_font = pygame.font.Font("data/fonts/OpenSans_Condensed-BoldItalic.ttf", 110)
        self.score_num = self.score_font.render(f"{score}", True, "#74A578")
        self.prompt = pygame.image.load("data/assets/play_again_prompt.png").convert_alpha()



        # Get coordinates
        self.score_num_rect = self.score_num.get_rect()
        self.score_num_rect.center = (GameContext.WIDTH/2, 300)
        self.score_intro_rect = self.score_intro.get_rect()
        self.score_intro_rect.center = (GameContext.WIDTH/2, 100)
        self.prompt_rect = self.prompt.get_rect()
        self.prompt_rect.center = (GameContext.WIDTH/2, GameContext.HEIGHT - 100)
        self.quip_rect = self.quip.get_rect()
        self.quip_rect.center = (GameContext.WIDTH/2, GameContext.HEIGHT - 150)




    # def update(self):
    

        

    def draw(self):
        # Method to draw on the screen
        
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.score_intro, self.score_intro_rect)
        self.screen.blit(self.score_num, self.score_num_rect)
        self.screen.blit(self.prompt, self.prompt_rect)
        self.screen.blit(self.quip, self.quip_rect)

       