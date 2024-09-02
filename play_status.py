from enum import Enum


class PlayStatus(Enum):
    CREDITS = 0
    MAIN_MENU = 1
    GAMEPLAY = 2
    GAME_OVER = 3
    GAME_END = 4
    TUTORIAL = 5


