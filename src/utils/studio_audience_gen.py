import pygame

def studio_audience_sfx(score):
    if 0 <= score <= 74:
        return pygame.mixer.music.load("data/assets/music/laugh_track_badplay.ogg")
    elif 74 <= score <= 149:
        return pygame.mixer.music.load("data/assets/music/laugh_track_okayplay.ogg")
    else: return pygame.mixer.music.load("data/assets/music/laugh_track_goodplay.ogg")

