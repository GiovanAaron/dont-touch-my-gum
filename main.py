import pygame
from sys import exit
from src.components.right_hand import RightHand

pygame.init()
screen = pygame.display.set_mode((360, 640), pygame.DOUBLEBUF)
pygame.display.set_caption("Don't Touch My Gum!")
clock = pygame.time.Clock()
test_font = pygame.font.Font("data/fonts/open_serif_italic.ttf", 32)

background = pygame.image.load('./data/assets/background.png').convert_alpha()
logo_surface = pygame.image.load('./data/assets/logo.png').convert_alpha()


player_surf = pygame.image.load('./data/assets/player_hand.png').convert_alpha()
player_mask = pygame.mask.from_surface(player_surf)
mask_image = player_mask.to_surface()



right_hand = RightHand(450,-100)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    mouse_x, mouse_y = pygame.mouse.get_pos()
    # print(f"Mouse position: ({mouse_x}, {mouse_y})")
    
    screen.blit(background, (0, 0))
    screen.blit(logo_surface, (62, 38))
    screen.blit(right_hand.image, right_hand.rect)
    
    right_hand.update()



    # Update the display
    pygame.display.update()
    clock.tick(60)
