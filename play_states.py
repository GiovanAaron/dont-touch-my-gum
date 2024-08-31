import pygame
from game_context import GameContext
from src.components.screens.credits import Credits
from play_status import PlayStatus
from src.components.screens.main_menu import MainMenu
from src.components.screens.gameplay import Gameplay
from src.components.screens.game_over import GameOver

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

    score = None  # Initialize score

    while GameContext.PLAY_STATE == PlayStatus.GAMEPLAY:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()



        score = gameplay.update()  # Ensure update returns the score

    # Return the score when the game is over
    return score



def game_over_state(score):
    game_over = GameOver(score)

    while GameContext.PLAY_STATE == PlayStatus.GAME_OVER:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        game_over.draw()
        pygame.display.flip()
        pygame.time.Clock().tick(60)

        keys = pygame.key.get_pressed()
        game_over.update(keys)


    # Handle transition back to the main menu or end
    if GameContext.PLAY_STATE == PlayStatus.MAIN_MENU:
        main_menu_state()
    elif GameContext.PLAY_STATE == PlayStatus.GAME_END:
        end_state()




def end_state():
    print("Game End State is running")
    pygame.quit()
    exit()
