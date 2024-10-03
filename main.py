import asyncio
import pygame
import random
import math

# Game Context
class GameContext:
    PLAY_STATE = None
    AUDIO = True
    HIGHEST_SCORE = 0
    MAIN_MENU_VISITS = 0
    TUTORIAL_VISITS = 0
    GAME_OVER_VISITS = 0
    SCREEN = None
    WIDTH = 360
    HEIGHT = 640

    def build_screen():
        screen = pygame.display.set_mode((GameContext.WIDTH, GameContext.HEIGHT))
        pygame.display.set_caption("Don't Touch My Gum!")
        icon = pygame.image.load("data/assets/tutorial/pygame_window_icon.png")
        pygame.display.set_icon(icon)
        GameContext.SCREEN = screen

# Play Status
class PlayStatus:
    CREDITS = 1
    MAIN_MENU = 2
    GAME_END = 3
    GAMEPLAY = 4
    GAME_OVER = 5
    TUTORIAL = 6
    END_CREDITS = 7

# Utils
def quip_gen(score):

    if 0 <= score <= 24:
        return pygame.image.load("data/assets/quips/_Did you even try__.png").convert_alpha()
    elif 25 <= score <= 49:
        return pygame.image.load("data/assets/quips/“yikes ... Better luck next time_”.png").convert_alpha()
    elif 50 <= score <= 74:
        return pygame.image.load("data/assets/quips/_Oof. That was rough._.png").convert_alpha()
    elif 75 <= score <= 99:
        return pygame.image.load("data/assets/quips/“You're getting there!_.png").convert_alpha()
    elif 100 <= score <= 124:
        return pygame.image.load("data/assets/quips/_Almost impressive._.png").convert_alpha()
    elif 125 <= score <= 149:
        return pygame.image.load("data/assets/quips/“Seen worse, done better.”.png").convert_alpha()
    elif 150 <= score <= 174:
        return pygame.image.load("data/assets/quips/_Keep pushing, champ._.png").convert_alpha()
    elif 175 <= score <= 199:
        return pygame.image.load("data/assets/quips/_Now we're talking!_.png").convert_alpha()
    elif 200 <= score <= 224:
        return pygame.image.load("data/assets/quips/“Impressive skills!”.png").convert_alpha()
    elif 225 <= score <= 249:
        return pygame.image.load("data/assets/quips/_You nailed it!_.png").convert_alpha()
    elif 250 <= score <= 299:
        return pygame.image.load("data/assets/quips/_Epic performance!_.png").convert_alpha()
    elif 300 <= score <= 349:
        return pygame.image.load("data/assets/quips/_You're unstoppable!_.png").convert_alpha()
    # elif 350 <= score <= 399:
    #     return pygame.image.load("").convert_alpha()
    # elif score <= 400:
    #     return pygame.image.load("").convert_alpha()
    else:
        return pygame.image.load("data/assets/quips/_You're unstoppable!_.png").convert_alpha()

def studio_audience_sfx(score):
    if 0 <= score <= 74:
        return pygame.mixer.music.load("data/assets/music/laugh_track_badplay.ogg")
    elif 74 <= score <= 149:
        return pygame.mixer.music.load("data/assets/music/laugh_track_okayplay.ogg")
    else: return pygame.mixer.music.load("data/assets/music/laugh_track_goodplay.ogg")


def sine_calculate():
    # sine calculate logic
    pass

def calculate_alpha():
    # calculate alpha logic
    pass

# Components
class RightHand:
    def __init__(self):
        # right hand logic
        pass

class LeftHand:
    def __init__(self):
        # left hand logic
        pass

class Player:
    def __init__(self):
        # player logic
        pass

class Background:
    def __init__(self):
        # background logic
        pass

class ScoreCount:
    def __init__(self):
        # score count logic
        pass

class MuteButton:
    def __init__(self):
        # mute button logic
        pass

class Paused:
    def __init__(self):
        # paused logic
        pass

class StartPrompt:
    def __init__(self):
        # start prompt logic
        pass

class HighestScore:
    def __init__(self):
        # highest score logic
        pass

class Mascot:
    def __init__(self):
        # mascot logic
        pass

class YellowSpark:
    def __init__(self):
        # yellow spark logic
        pass

class WhiteSparkle:
    def __init__(self):
        # white sparkle logic
        pass

class Backbutton:
    def __init__(self):
        # back button logic
        pass

class MainMenuButton:
    def __init__(self):
        # main menu button logic
        pass

class TutorialIcon:
    def __init__(self):
        # tutorial icon logic
        pass

class PlayAgainPrompt:
    def __init__(self):
        # play again prompt logic
        pass

# Screens
class GameOver:
    def __init__(self):
        # game over screen logic
        pass

class MainMenu:
    def __init__(self):
        # main menu screen logic
        pass

class Gameplay:
    def __init__(self):
        # gameplay screen logic
        pass

class Tutorial:
    def __init__(self):
        # tutorial screen logic
        pass

class Credits:
     def __init__(self):
       
        # Ensure the screen is set up before accessing it
        GameContext.build_screen()
        self.screen = GameContext.SCREEN
        self.timer = 0

        # Load images and set up background
        self.bg = pygame.Surface(self.screen.get_size())
        self.bg.fill((255, 255, 255))
        
        # Load images with proper method call
        self.personal_logo = pygame.image.load("data/assets/ui/giovan_aaron.png").convert_alpha()
        self.personal_caption = pygame.image.load("data/assets/ui/caption.png").convert_alpha()
        self.DTMG_logo = pygame.image.load("data/assets/ui/logo.png")

        self.personal_logo_rect = self.personal_logo.get_rect()
        self.personal_logo_rect.center = (GameContext.WIDTH/2, GameContext.HEIGHT/2)
        
        self.DTMG_logo_rect = self.DTMG_logo.get_rect()
        self.DTMG_logo_rect.center = (GameContext.WIDTH/2, 100)

        self.personal_caption_rect = self.personal_caption.get_rect()
        self.personal_caption_rect.center = (GameContext.WIDTH/2, 600)

     def update(self):
        self.timer += 1/60
        
        if self.timer >= 3:
            GameContext.PLAY_STATE = PlayStatus.MAIN_MENU

        

     def draw(self):
        # Method to draw on the screen
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.personal_logo, self.personal_logo_rect)  # Adjust position as needed
        self.screen.blit(self.personal_caption, self.personal_caption_rect)  # Adjust position as needed
        self.screen.blit(self.DTMG_logo, self.DTMG_logo_rect)  # Adjust position as needed


class EndCredits:
    def __init__(self):
        # end credits screen logic
        pass

# Play States
async def credits_state():
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

async def end_state():
    # end state logic
    pass

async def main_menu_state():
    # main menu state logic
    pass

async def gameplay_state():
    # gameplay state logic
    pass

async def game_over_state(score):
    # game over state logic
    pass

async def tutorial_state():
    # tutorial state logic
    pass

async def end_credits_state():
    # end credits state logic
    pass

# Main
async def main():
    while True:
        await asyncio.sleep(0)  # Yield control to the event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        GameContext.PLAY_STATE = PlayStatus.CREDITS

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
    pygame.init()
    GameContext.build_screen()
    asyncio.run(main())