import pygame
from game_context import GameContext
from play_status import PlayStatus
from play_states import credits_state, end_state, main_menu_state, gameplay_state, game_over_state, tutorial_state, end_credits_state

pygame.init()

FPS = pygame.time.Clock()
GameContext.build_screen()

def update_display():
    pygame.display.update()
    FPS.tick(60)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if GameContext.PLAY_STATE == PlayStatus.CREDITS:
            credits_state()

        elif GameContext.PLAY_STATE == PlayStatus.MAIN_MENU:
            main_menu_state()

        elif GameContext.PLAY_STATE == PlayStatus.GAME_END:
            end_state()

        elif GameContext.PLAY_STATE == PlayStatus.GAMEPLAY:
            score = gameplay_state()  # Retrieve the score when gameplay ends

        elif GameContext.PLAY_STATE == PlayStatus.GAME_OVER:
            try:
                score
                game_over_state(score)
            except: game_over_state()  # Pass the score to the game over state
        elif GameContext.PLAY_STATE == PlayStatus.TUTORIAL:
            tutorial_state()

        elif GameContext.PLAY_STATE == PlayStatus.END_CREDITS:
            end_credits_state()

if __name__ == "__main__":
    main()
