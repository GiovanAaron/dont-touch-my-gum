import pygame

from sys import exit
from src.components.right_hand import RightHand
from src.components.left_hand import LeftHand
from src.components.player import Player
from src.components.background import Background
from src.components.score import ScoreCount
import random

pygame.init()
screen = pygame.display.set_mode((360, 640), pygame.DOUBLEBUF)
pygame.display.set_caption("Don't Touch My Gum!")
clock = pygame.time.Clock()

# Load assets
background = pygame.image.load('./data/assets/background.png').convert_alpha()
logo_surface = pygame.image.load('./data/assets/logo.png').convert_alpha()
scroll_bg = Background()
score_container = ScoreCount()


player = Player(244,622)

# Initialize sprite groups
right_hands = pygame.sprite.Group()
left_hands = pygame.sprite.Group()

# Initialize first RightHand and LeftHand
right_hands.add(RightHand(450, -100))
left_hands.add(LeftHand(-450, -200))

# Timing variables for spawning new instances
last_left_hand_spawn_time = pygame.time.get_ticks()
last_right_hand_spawn_time = pygame.time.get_ticks()
left_hand_spawn_interval = random.randint(4000, 8000)  # Spawn new LeftHand every 4-8 seconds
right_hand_spawn_interval = random.randint(4000, 8000)  # Spawn new RightHand every 4-8 seconds

# testing/debugging
test_font = pygame.font.Font("data/fonts/open_serif_italic.ttf", 32)
collision_notif = test_font.render("You're hit!", True, "Red")


def check_collision(sprite1, sprite2):
    # Calculate the offset of sprite2 relative to sprite1
    offset = (sprite2.rect.x - sprite1.collision_rect.x, sprite2.rect.y - sprite1.collision_rect.y)
    # Check if there is an overlap between the masks
    return sprite1.collision_mask.overlap(sprite2.mask, offset) is not None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    mouse_x, mouse_y = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    

   
    # Screen background and static elements
    # screen.blit(background, (0, 0))
    # screen.blit(logo_surface, (62, 38))

    # Get current time
    current_time = pygame.time.get_ticks()

    screen.blit(scroll_bg.image, scroll_bg.rect)
    screen.blit(scroll_bg.image2, scroll_bg.rect2)
    scroll_bg.update()
    scroll_bg.draw(screen)

    # Check if we need to spawn a new LeftHand
    if current_time - last_left_hand_spawn_time > left_hand_spawn_interval:
        # Only spawn a new LeftHand if there are fewer than 2 on the screen
        if len(left_hands) < 2:
            last_left_hand_spawn_time = current_time
            left_hand_spawn_interval = random.randint(4000, 8000)  # Randomize the interval again
            new_left_hand = LeftHand(random.randint(-190, -40), -150)  # Randomize x position within bounds
            left_hands.add(new_left_hand)

    # Check if we need to spawn a new RightHand
    if current_time - last_right_hand_spawn_time > right_hand_spawn_interval:
        # Only spawn a new RightHand if there are fewer than 2 on the screen
        if len(right_hands) < 2:
            last_right_hand_spawn_time = current_time
            right_hand_spawn_interval = random.randint(4000, 8000)  # Randomize the interval again
            new_right_hand = RightHand(random.randint(100, 450), -100)  # Randomize x position within bounds
            right_hands.add(new_right_hand)

    
    screen.blit(player.collision_image, player.collision_rect)
    screen.blit(player.image, player.rect)
    player.update(keys)
    for right_hand in right_hands:
        if check_collision(player, right_hand):
            # print("Collision with RightHand!")
            screen.blit(collision_notif, (150, 250))
    for left_hand in left_hands:
        if check_collision(player, left_hand):
            # print("Collision with RightHand!")
            screen.blit(collision_notif, (150, 250))


    # Update and draw RightHand group
    right_hands.update()
    right_hands.draw(screen)
    
    # Update and draw LeftHand group
    left_hands.update()
    left_hands.draw(screen)

    screen.blit(score_container.image, score_container.rect)
    score_container.update()
    score_container.draw(screen)


    # Update the display
    pygame.display.update()
    clock.tick(60)
