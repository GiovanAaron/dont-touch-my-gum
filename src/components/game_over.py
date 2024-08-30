import pygame
from game_context import GameContext
from play_status import PlayStatus




class GameOver():
    def __init__(self, score):
        print(f"Game Over! Your score was: {score}")
        # Ensure the screen is set up before accessing it
        GameContext.build_screen()
        self.screen = GameContext.SCREEN
        self.bg = pygame.Surface(self.screen.get_size())
        self.bg.fill((255, 255, 255))
        

    # def update(self):
    

        

    def draw(self):
        # Method to draw on the screen
        self.screen.blit(self.bg, (0, 0))
       