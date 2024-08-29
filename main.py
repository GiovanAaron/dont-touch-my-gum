import pygame
from game_context import GameContext
from play_status import PlayStatus
from play_states import credits_state



pygame.init()

FPS = pygame.time.Clock()

def update_display():
    pygame.display.update()
    FPS.tick(60)


#Credits Assets:
  

def main():
    while True:
        if GameContext.PLAY_STATE == PlayStatus.CREDITS:
            credits_state()

        if GameContext.PLAY_STATE == PlayStatus.GAME_END:
            print("hello!")
            pygame.quit()
            exit()


if __name__ == "__main__":
    main()