import pygame
from game_context import GameContext
from src.components.credits import Credits  # Adjust import as needed
from play_status import PlayStatus  # Ensure PlayStatus is imported correctly

def credits_state():
    # Initialize credits component
    credits = Credits()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        # Update credits state
        credits.update()

        # Check if the play state has changed
        if GameContext.PLAY_STATE == PlayStatus.GAME_END:
            print("Play state changed to GAME_END")
            
            end_state()
            break
            

        # Draw credits
        credits.draw()
        
        pygame.display.flip()
        pygame.time.Clock().tick(60)  # Cap the frame rate to 60 FPS

def end_state():
        pygame.quit()
        exit()
