import asyncio
import pygame
from game_context import GameContext
from play_status import PlayStatus
from play_states import credits_state, end_state, main_menu_state, gameplay_state, game_over_state, tutorial_state, end_credits_state

pygame.init()

async def main():
    while True:
        await asyncio.sleep(0)  # Yield control to the event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if GameContext.PLAY_STATE == PlayStatus.CREDITS:
            await credits_state()

        elif GameContext.PLAY_STATE == PlayStatus.MAIN_MENU:
            await main_menu_state()

        elif GameContext.PLAY_STATE == PlayStatus.GAME_END:
            await end_state()

        elif GameContext.PLAY_STATE == PlayStatus.GAMEPLAY:
            score = await gameplay_state()  # Retrieve the score when gameplay ends

        elif GameContext.PLAY_STATE == PlayStatus.GAME_OVER:
            try:
                score
                await game_over_state(score)
            except: await game_over_state()  # Pass the score to the game over state
        elif GameContext.PLAY_STATE == PlayStatus.TUTORIAL:
            await tutorial_state()

        elif GameContext.PLAY_STATE == PlayStatus.END_CREDITS:
            await end_credits_state()

if __name__ == "__main__":
    asyncio.run(main())