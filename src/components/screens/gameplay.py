import pygame
from game_context import GameContext
from play_status import PlayStatus
from src.components.gameplay.right_hand import RightHand
from src.components.gameplay.left_hand import LeftHand
from src.components.gameplay.player import Player
from src.components.gameplay.background import Background
from src.components.gameplay.score import ScoreCount
from src.components.gameplay.mute_toggle import MuteButton
import random


class Gameplay:
    def __init__(self):
        # Initialize Pygame
        pygame.mixer.init()
        self.screen = GameContext.SCREEN
        self.clock = pygame.time.Clock()

        # Load Music
        pygame.mixer.music.load("data/assets/music/dtmg.ogg")
        pygame.mixer.music.play(-1)



        # Load assets
        self.background = pygame.image.load('./data/assets/background.png').convert_alpha()
        self.scroll_bg = Background()
        self.score_container = ScoreCount()

        self.player = Player(244, 622)


        # Initialize mute button
        self.mute_button = MuteButton()


        # Initialize sprite groups
        self.right_hands = pygame.sprite.Group()
        self.left_hands = pygame.sprite.Group()

        # Initialize first RightHand and LeftHand
        self.right_hands.add(RightHand(450, -100))
        self.left_hands.add(LeftHand(-450, -200))

        # Timing variables for spawning new instances
        self.last_left_hand_spawn_time = pygame.time.get_ticks()
        self.last_right_hand_spawn_time = pygame.time.get_ticks()
        self.left_hand_spawn_interval = random.randint(4000, 8000)  # Spawn new LeftHand every 4-8 seconds
        self.right_hand_spawn_interval = random.randint(4000, 8000)  # Spawn new RightHand every 4-8 seconds

        # Font and collision notification
        self.test_font = pygame.font.Font("data/fonts/open_serif_italic.ttf", 32)
        self.collision_notif = self.test_font.render("You're hit!", True, "Red")

        

    def check_collision(self, sprite1, sprite2):
        # Calculate the offset of sprite2 relative to sprite1
        offset = (sprite2.rect.x - sprite1.collision_rect.x, sprite2.rect.y - sprite1.collision_rect.y)
        # Check if there is an overlap between the masks
        return sprite1.collision_mask.overlap(sprite2.mask, offset) is not None

    def draw(self):
        # Draw screen background and static elements
        self.screen.blit(self.scroll_bg.image, self.scroll_bg.rect)
        self.screen.blit(self.scroll_bg.image2, self.scroll_bg.rect2)

        # Draw player
        self.screen.blit(self.player.collision_image, self.player.collision_rect)
        self.screen.blit(self.player.image, self.player.rect)

        # Draw RightHand and LeftHand groups
        self.right_hands.draw(self.screen)
        self.left_hands.draw(self.screen)

        self.mute_button.draw(self.screen)

        # Draw score container
        self.score_container.draw(self.screen)  
        
        self.player.draw(self.screen)# Ensure draw() method in ScoreCount class blits the score correctly

    def update(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # 1 is the left mouse button
                        mouse_pos = pygame.mouse.get_pos()

                    self.mute_button.update(mouse_pos)

            mouse_x, mouse_y = pygame.mouse.get_pos()
            keys = pygame.key.get_pressed()

            

            # Update background scrolling
            self.scroll_bg.update()

            # Get current time
            current_time = pygame.time.get_ticks()

            # Check if we need to spawn a new LeftHand
            if current_time - self.last_left_hand_spawn_time > self.left_hand_spawn_interval:
                if len(self.left_hands) < 2:
                    self.last_left_hand_spawn_time = current_time
                    self.left_hand_spawn_interval = random.randint(4000, 8000)  # Randomize the interval again
                    new_left_hand = LeftHand(random.randint(-190, -40), -150)  # Randomize x position within bounds
                    self.left_hands.add(new_left_hand)

            # Check if we need to spawn a new RightHand
            if current_time - self.last_right_hand_spawn_time > self.right_hand_spawn_interval:
                if len(self.right_hands) < 2:
                    self.last_right_hand_spawn_time = current_time
                    self.right_hand_spawn_interval = random.randint(4000, 8000)  # Randomize the interval again
                    new_right_hand = RightHand(random.randint(100, 450), -100)  # Randomize x position within bounds
                    self.right_hands.add(new_right_hand)

            # Update player
            self.player.update(keys)

            # Check for collisions with RightHand
            for right_hand in self.right_hands:
                if self.check_collision(self.player, right_hand):
                    self.screen.blit(self.collision_notif, (150, 250))
                    GameContext.PLAY_STATE = PlayStatus.GAME_OVER
                    pygame.display.update()
                    return self.score_container.get_final_score()

            # Check for collisions with LeftHand
            for left_hand in self.left_hands:
                if self.check_collision(self.player, left_hand):
                    self.screen.blit(self.collision_notif, (150, 250))
                    GameContext.PLAY_STATE = PlayStatus.GAME_OVER
                    pygame.display.update()
                    return self.score_container.get_final_score()

            # Update RightHand and LeftHand groups
            self.right_hands.update()
            self.left_hands.update()

            # Update score container
            self.score_container.update()

            
            # Draw everything
            self.draw()


            # Handle audio mute/unmute
            if GameContext.AUDIO:
                pygame.mixer.music.set_volume(1.0)  # Unmuted state
            else:
                pygame.mixer.music.set_volume(0.0)  # Muted state



            # Update the display
            pygame.display.update()
            self.clock.tick(60)