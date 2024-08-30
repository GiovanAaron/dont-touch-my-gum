import pygame

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
        

