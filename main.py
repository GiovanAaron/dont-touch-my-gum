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
test_surface = test_font.render('My Game', True, "Grey")


lhs_x_pos = 0
lhs_y_pos = 30

left_hand_surface = pygame.image.load('./data/assets/enemy_left_hand.png').convert_alpha()
left_hand_rect = left_hand_surface.get_rect(center = (lhs_x_pos, lhs_y_pos))



phs_x_pos = 360 / 1.5
phs_y_pos = 650

player_surf = pygame.image.load('./data/assets/player_hand.png').convert_alpha()
player_rect = player_surf.get_rect(center=(phs_x_pos, phs_y_pos))
player_mask = pygame.mask.from_surface(player_surf)
mask_image = player_mask.to_surface()

time_counter = 0
amplitude = 4  # Adjust this value for the intensity of the sine wave effect
frequency = 0.1  # Adjust this for the speed of oscillation


right_hand = RightHand((150,150))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        phs_x_pos -= 4
        
    if keys[pygame.K_RIGHT]:
        phs_x_pos += 4

    if keys[pygame.K_UP]:
        phs_y_pos -= 4

    if keys[pygame.K_DOWN]:
        phs_y_pos += 4

    player_rect.center = (phs_x_pos, phs_y_pos)
    left_hand_rect.center = (lhs_x_pos, lhs_y_pos)


      # screen.blit(mask_image, player_rect)
    # Drawing
    screen.blit(background, (0, 0))
    screen.blit(logo_surface, (62, 38))
    screen.blit(player_surf, player_rect)
    lhs_x_pos -= 1
    lhs_y_pos += 1

    if lhs_x_pos < -300: lhs_x_pos = -10
    if lhs_y_pos > 640: lhs_y_pos = 30
    
    screen.blit(left_hand_surface, left_hand_rect)
    # screen.blit(right_hand.image, right_hand.rect)
    
  
    pygame.draw.rect(screen, (255, 0, 0), player_rect, 1)  # Red outline for player hitbox
    pygame.draw.rect(screen, (0, 255, 0), left_hand_rect, 1)
    
    if player_rect.colliderect(left_hand_rect):
        print('collision detected')

    # Update the display
    pygame.display.update()
    clock.tick(60)
