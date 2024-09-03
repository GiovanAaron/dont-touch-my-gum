import pygame



from play_status import PlayStatus


class GameContext:
    PLAY_STATE = PlayStatus.GAME_OVER
    AUDIO = True
    HIGHEST_SCORE = 0
    
    SCREEN = None
    WIDTH = 360
    HEIGHT = 640


    # @staticmethod
    def build_screen():
        screen = pygame.display.set_mode((360, 640))
        pygame.display.set_caption("Don't Touch My Gum!")
        icon = pygame.image.load("data/assets/tutorial/pygame_window_icon.png")
        pygame.display.set_icon(icon)

        GameContext.SCREEN = screen


