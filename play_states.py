import pygame
from game_context import GameContext
from src.components.credits import Credits
from play_status import PlayStatus
from src.components.main_menu import MainMenu
from src.components.gameplay import Gameplay

def credits_state():
    credits = Credits()
    
    while GameContext.PLAY_STATE == PlayStatus.CREDITS:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        credits.update()
        credits.draw()
        
        pygame.display.flip()
        pygame.time.Clock().tick(60)  # Cap the frame rate to 60 FPS

    # When exiting the loop, check the new state
    if GameContext.PLAY_STATE == PlayStatus.MAIN_MENU:
        main_menu_state()

def main_menu_state():
    main_menu = MainMenu()

    while GameContext.PLAY_STATE == PlayStatus.MAIN_MENU:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        keys = pygame.key.get_pressed()


        main_menu.draw()
        main_menu.update(keys)

        pygame.display.flip()
        pygame.time.Clock().tick(60)  # Cap the frame rate to 60 FPS


def gameplay_state():
    gameplay = Gameplay()
    
    
    while GameContext.PLAY_STATE == PlayStatus.MAIN_MENU:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    
    # keys = pygame.key.get_pressed()
    gameplay.update()
    



def end_state():
    print("Game End State is running")
    pygame.quit()
    exit()
