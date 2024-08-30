import pygame



from play_status import PlayStatus


class GameContext:
    PLAY_STATE = PlayStatus.CREDITS
    
    SCREEN = None
    WIDTH = 360
    HEIGHT = 640


    # @staticmethod
    def build_screen():
        screen = pygame.display.set_mode((360, 640))
        pygame.display.set_caption("Don't Touch My Gum!")

        GameContext.SCREEN = screen


