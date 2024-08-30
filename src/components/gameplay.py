import pygame
from game_context import GameContext
from play_status import PlayStatus
from src.components.right_hand import RightHand
from src.components.left_hand import LeftHand
from src.components.player import Player
from src.components.background import Background
from src.components.score import ScoreCount
import random




class Gameplay:
    def __init__(self):
        # Initialize Pygame
        GameContext.build_screen()
        self.screen = GameContext.SCREEN
        self.clock = pygame.time.Clock()

        # Load assets
        self.background = pygame.image.load('./data/assets/background.png').convert_alpha()
        self.logo_surface = pygame.image.load('./data/assets/logo.png').convert_alpha()
        self.scroll_bg = Background()
        self.score_container = ScoreCount()
        
        self.player = Player(244, 622)

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

    def update(self):
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            mouse_x, mouse_y = pygame.mouse.get_pos()
            keys = pygame.key.get_pressed()

            # Screen background and static elements
            self.screen.blit(self.scroll_bg.image, self.scroll_bg.rect)
            self.screen.blit(self.scroll_bg.image2, self.scroll_bg.rect2)
            self.scroll_bg.update()
            self.scroll_bg.draw(self.screen)

            # Get current time
            current_time = pygame.time.get_ticks()

            # Check if we need to spawn a new LeftHand
            if current_time - self.last_left_hand_spawn_time > self.left_hand_spawn_interval:
                # Only spawn a new LeftHand if there are fewer than 2 on the screen
                if len(self.left_hands) < 2:
                    self.last_left_hand_spawn_time = current_time
                    self.left_hand_spawn_interval = random.randint(4000, 8000)  # Randomize the interval again
                    new_left_hand = LeftHand(random.randint(-190, -40), -150)  # Randomize x position within bounds
                    self.left_hands.add(new_left_hand)

            # Check if we need to spawn a new RightHand
            if current_time - self.last_right_hand_spawn_time > self.right_hand_spawn_interval:
                # Only spawn a new RightHand if there are fewer than 2 on the screen
                if len(self.right_hands) < 2:
                    self.last_right_hand_spawn_time = current_time
                    self.right_hand_spawn_interval = random.randint(4000, 8000)  # Randomize the interval again
                    new_right_hand = RightHand(random.randint(100, 450), -100)  # Randomize x position within bounds
                    self.right_hands.add(new_right_hand)

            # Update and draw game elements
            self.screen.blit(self.player.collision_image, self.player.collision_rect)
            self.screen.blit(self.player.image, self.player.rect)
            self.player.update(keys)

            for right_hand in self.right_hands:
                if self.check_collision(self.player, right_hand):
                    self.screen.blit(self.collision_notif, (150, 250))
                    GameContext.PLAY_STATE = PlayStatus.MAIN_MENU
                    pygame.display.update()
                    return

            for left_hand in self.left_hands:
                if self.check_collision(self.player, left_hand):
                    self.screen.blit(self.collision_notif, (150, 250))
                    GameContext.PLAY_STATE = PlayStatus.MAIN_MENU
                    pygame.display.update()
                    return
                    

            # Update and draw RightHand group
            self.right_hands.update()
            self.right_hands.draw(self.screen)

            # Update and draw LeftHand group
            self.left_hands.update()
            self.left_hands.draw(self.screen)

            self.screen.blit(self.score_container.image, self.score_container.rect)
            self.score_container.update()
            self.score_container.draw(self.screen)

            # Update the display
            pygame.display.update()
            self.clock.tick(60)
