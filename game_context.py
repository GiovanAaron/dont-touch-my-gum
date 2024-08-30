import pygame



from play_status import PlayStatus


class GameContext:
    PLAY_STATE = PlayStatus.GAMEPLAY
    
    SCREEN = None
    WIDTH = 360
    HEIGHT = 640


    # @staticmethod
    def build_screen():
        screen = pygame.display.set_mode((360, 640))
        GameContext.SCREEN = screen


