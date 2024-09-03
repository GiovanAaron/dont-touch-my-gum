import pygame
from game_context import GameContext
from src.components.screens.credits import Credits
from play_status import PlayStatus
from src.components.screens.main_menu import MainMenu
from src.components.screens.gameplay import Gameplay
from src.components.screens.game_over import GameOver
from src.components.screens.tutorial import Tutorial
from src.components.ui.back import Backbutton
from src.components.ui.main_menu import MainMenuButton
from src.components.ui.tutorial_icon import TutorialIcon
from src.components.screens.end_credits import EndCredits

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



def game_over_state(score=0):
    game_over = GameOver(score)
    main_menu_nav = MainMenuButton()
    tutorial_icon = TutorialIcon()

    while GameContext.PLAY_STATE == PlayStatus.GAME_OVER:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if event.button == 1:  # Left mouse button
                        mouse_pos = pygame.mouse.get_pos()
                        
                        if main_menu_nav.is_clicked(mouse_pos):
                            
                            GameContext.PLAY_STATE = PlayStatus.MAIN_MENU

            if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if event.button == 1:  # Left mouse button
                        mouse_pos = pygame.mouse.get_pos()
                        
                        if tutorial_icon.is_clicked(mouse_pos):
                            
                            GameContext.PLAY_STATE = PlayStatus.TUTORIAL


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



def tutorial_state():

    tutorial = Tutorial()
    back_button = Backbutton()
    while GameContext.PLAY_STATE == PlayStatus.TUTORIAL:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    
                    if back_button.is_clicked(mouse_pos):
                        
                        GameContext.PLAY_STATE = PlayStatus.MAIN_MENU
    
        
        keys = pygame.key.get_pressed()

        tutorial.update(keys)
        tutorial.draw()
        pygame.time.Clock().tick(60)
        


def end_credits_state():

    end_credits = EndCredits()
    while GameContext.PLAY_STATE == PlayStatus.END_CREDITS:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        keys = pygame.key.get_pressed()
        end_credits.draw()
        end_credits.update(keys)

def end_state():
    print("Game End State is running")
    pygame.quit()
    exit()
