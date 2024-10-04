import asyncio
import pygame
import random
import math


if __import__('sys').platform == "emscripten":
    import js

pygame.init()

# Play Status
class PlayStatus:
    CREDITS = 1
    MAIN_MENU = 2
    GAME_END = 3
    GAMEPLAY = 4
    GAME_OVER = 5
    TUTORIAL = 6
    END_CREDITS = 7

# Game Context
class GameContext:
    PLAY_STATE = PlayStatus.CREDITS
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


def sine_calculate(base_y, timer, amplitude=5, frequency=0.015):
    """
    Calculate the new y position using a sine wave for smooth movement.
    
    :param base_y: The base y position around which the object will hover.
    :param timer: A timer value to feed into the sine function to simulate time.
    :param amplitude: The maximum distance the object will move from the base y position.
    :param frequency: How fast the object will move up and down (lower values = slower).
    :return: The new y position.
    """
    return base_y + amplitude * math.sin(frequency * timer)

def calculate_alpha(y):
    # Known points
    y1, alpha1 = 350, 0
    y2, alpha2 = 230, 255
    
    # Calculate the slope (m)
    m = (alpha2 - alpha1) / (y2 - y1)
    
    # Calculate the y-intercept (b)
    b = alpha1 - m * y1
    
    # Calculate the alpha value based on y-coordinate
    alpha = m * y + b
    
    # Ensure the alpha is within the range [0, 255]
    alpha = max(0, min(255, alpha))
    
    return int(alpha)

# Components

class LinkedIn(pygame.sprite.Sprite):

    def __init__(self):
        self.image = pygame.image.load("data/assets/ui/linkedin.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (GameContext.WIDTH - 50, 20)

    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

class RightHand(pygame.sprite.Sprite):
    LEFT_BOUNDARY = 100
    RIGHT_BOUNDARY = 450
    SOFT_LEFT_THRESHOLD = 200  # Soft boundary for left movement
    SOFT_RIGHT_THRESHOLD = 290  # Soft boundary for right movement

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("data/assets/enemy_right_hand.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = random.uniform(0.735, 3.5)  # Slower baseline speed, similar to LeftHand
        self.direction = False  # True = left, False = right
        self.timer = 0
        self.soft_boundary_chance = 0.7  # Chance to respect soft boundaries

        # Randomized parameters for sine wave movement
        self.amplitude = random.uniform(30, 70)  # Random amplitude between 30 and 70
        self.frequency = random.uniform(0.005, 0.02)  # Slower frequency for sine wave, similar to LeftHand
        self.original_x = x  # Store the original x position for sine calculation

        # mask
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.timer += 4
        
        # Update speed every 120 frames (slower updates)
        if self.timer % 120 == 0:
            self.speed = random.uniform(0.5, 2)  # Slower speed range, similar to LeftHand

        # Calculate sine wave movement
        sine_offset = self.amplitude * math.sin(self.frequency * self.timer)
        self.rect.x = self.original_x + sine_offset

        # Decide whether to respect soft boundaries or move to hard boundaries
        follow_soft_boundary = random.random() < self.soft_boundary_chance

        if follow_soft_boundary:
            # Soft left boundary logic
            if self.direction and self.rect.x < self.SOFT_LEFT_THRESHOLD:
                self.direction = False

            # Soft right boundary logic
            if not self.direction and self.rect.x > self.SOFT_RIGHT_THRESHOLD:
                self.direction = True
        else:
            # Hard boundaries logic
            if self.rect.x > self.RIGHT_BOUNDARY:
                self.direction = True
            if self.rect.x < self.LEFT_BOUNDARY:
                self.direction = False

        # Update original_x to maintain smooth sine wave movement
        if self.direction:
            self.original_x -= self.speed
        else:
            self.original_x += self.speed

        # Vertical movement logic
        if self.rect.y > 650:
            self.rect.y = -100
        self.rect.y += self.speed / 2 + 0.5

        self.mask.set_at((self.rect.x - self.rect.left, self.rect.y - self.rect.top), 1)

class LeftHand(pygame.sprite.Sprite):
    LEFT_BOUNDARY = -190  # Hard left boundary
    RIGHT_BOUNDARY = -40  # Hard right boundary
    SOFT_LEFT_THRESHOLD = -160  # Soft boundary for left movement
    SOFT_RIGHT_THRESHOLD = -70  # Soft boundary for right movement

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("data/assets/enemy_left_hand.png")  # Use the left hand image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = random.uniform(0.85, 4.8)  # Slower baseline speed
        self.direction = True  # True = left, False = right (start moving left)
        self.timer = 0
        self.soft_boundary_chance = 0.7  # Chance to respect soft boundaries

        # Randomized parameters for sine wave movement
        self.amplitude = random.uniform(30, 70)  # Random amplitude between 30 and 70
        self.frequency = random.uniform(0.005, 0.02)  # Slower frequency for sine wave
        self.original_x = x  # Store the original x position for sine calculation

        # mask
        self.mask = pygame.mask.from_surface(self.image)


        # Variables for Y-axis speed boost logic
        self.last_speed_change_time = pygame.time.get_ticks()  # Track the last time the speed was changed
        self.speed_boost_duration = 5000  # 5 seconds in milliseconds
        self.y_speed_multiplier = 1  # Multiplier for Y-axis speed
        self.is_boosted = False  # To track if speed is currently boosted

    def update(self):
        self.timer += 4
        
        # Slow down the rate of speed updates
        if self.timer % 120 == 0:  # Slower updates every 120 frames
            self.speed = random.uniform(0.5, 2)  # Slower speed range

        # Check if 5 seconds have passed for the Y-axis speed boost logic
        current_time = pygame.time.get_ticks()
        if current_time - self.last_speed_change_time >= self.speed_boost_duration:
            self.last_speed_change_time = current_time  # Reset the timer
            if random.random() < 0.5:  # 50% chance to apply a speed boost
                self.y_speed_multiplier = 2  # Double the speed
                self.is_boosted = True
            else:
                self.y_speed_multiplier = 1  # Maintain normal speed
                self.is_boosted = False

        # If speed is boosted, reset it after a short burst
        if self.is_boosted and current_time - self.last_speed_change_time >= 1000:  # 1 second boost duration
            self.y_speed_multiplier = 1  # Return to normal speed
            self.is_boosted = False

        # Calculate sine wave movement for horizontal (X-axis) movement
        sine_offset = self.amplitude * math.sin(self.frequency * self.timer)
        self.rect.x = self.original_x + sine_offset

        # Decide whether to respect soft boundaries or move to hard boundaries
        follow_soft_boundary = random.random() < self.soft_boundary_chance

        if follow_soft_boundary:
            # Soft left boundary logic
            if self.direction and self.rect.x < self.SOFT_LEFT_THRESHOLD:
                self.direction = False

            # Soft right boundary logic
            if not self.direction and self.rect.x > self.SOFT_RIGHT_THRESHOLD:
                self.direction = True
        else:
            # Hard boundaries logic
            if self.rect.x < self.LEFT_BOUNDARY:
                self.direction = False
            if self.rect.x > self.RIGHT_BOUNDARY:
                self.direction = True

        # Update original_x to maintain smooth sine wave movement
        if self.direction:
            self.original_x -= self.speed
        else:
            self.original_x += self.speed

        # Vertical (Y-axis) movement logic with speed multiplier
        if self.rect.y > 650:
            self.rect.y = -250
        self.rect.y += (self.speed / 2 + 0.5) * self.y_speed_multiplier

        self.mask.set_at((self.rect.x - self.rect.left, self.rect.y - self.rect.top), 1)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("data/assets/player_hand2.png").convert_alpha()  # Load the player's image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 6  # Speed at which the player moves

        # self.mask = pygame.mask.from_surface(self.image)

         # Create an invisible cropped mask for collision detection
        self.collision_image = pygame.image.load("data/assets/gum_with_buffer.png").convert_alpha()
        self.collision_rect = self.collision_image.get_rect()
        self.collision_buffer_x = 35
        self.collision_buffer_y = 14
        self.collision_rect.center = (x + self.collision_buffer_x , self.collision_buffer_y )
        self.collision_mask = pygame.mask.from_surface(self.collision_image)
        self.collision_image.set_alpha(0)

        # boundary
        self.left_boundary = pygame.image.load("data/assets/boundary.png").convert_alpha()
        self.right_boundary = pygame.image.load("data/assets/boundary.png").convert_alpha()
        self.left_boundary_rect = self.left_boundary.get_rect()
        self.left_boundary_rect.topleft = (0, 237)
        self.right_boundary_rect = self.left_boundary.get_rect()
        self.right_boundary_rect.topleft = (270, 237)

        self.boundary_opacity = 0

        

    def update(self, keys):
        # Move the player based on key presses
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

        self.collision_rect.x = self.rect.x + self.collision_buffer_x
        self.collision_rect.y = self.rect.y + self.collision_buffer_y

        # Keep the player within the screen bounds
        self.rect.x = max(-50, min(self.rect.x, 575 - self.rect.width))
        self.rect.y = max(230, min(self.rect.y, 1000 - self.rect.height))

        self.collision_rect.center = self.collision_rect.center

        
        self.bounadry_opacity = calculate_alpha(self.rect.y) 
        self.left_boundary.set_alpha(self.bounadry_opacity)
        self.right_boundary.set_alpha(self.bounadry_opacity)

        

    def draw(self, surface):
        
        surface.blit(self.left_boundary, self.left_boundary_rect)
        surface.blit(self.right_boundary, self.right_boundary_rect)

class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("data/assets/background.png")
        self.image2 = pygame.image.load("data/assets/background.png")
        self.rect = self.image.get_rect()
        self.rect2 = self.image2.get_rect()
        self.rect.topleft = (0, 0)
        self.rect2.topleft = (0, -self.rect.height)
        self.speed = 2

    def update(self):
        # Move both images down
        self.rect.y += self.speed
        self.rect2.y += self.speed

        # If the first image moves off the screen, reset it to the top
        if self.rect.y >= self.rect.height:
            self.rect.y = -self.rect.height

        # If the second image moves off the screen, reset it to the top
        if self.rect2.y >= self.rect2.height:
            self.rect2.y = -self.rect2.height

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.image2, self.rect2)

class ScoreCount(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # Initialize the Sprite superclass
        self.image = pygame.image.load("data/assets/score_container.png")
        self.rect = self.image.get_rect()
        self.rect.center = (360 / 2, 80)
        self.score = 0
        self.score_font = pygame.font.Font("data/fonts/OpenSans_Condensed-BoldItalic.ttf", 25)
        self.update_score_text()  # Initialize score_num with the correct score

        # Timer variables
        self.last_update_time = pygame.time.get_ticks()  # Get the current time
        self.update_interval = 3000  # 5000 milliseconds = 5 seconds

    def update_score_text(self):
        # Correct the string interpolation for the score
        self.score_num = self.score_font.render(f"{self.score}", True, "#74A578")

    def update(self):
        # Get the current time
        current_time = pygame.time.get_ticks()

        # Check if 5 seconds have passed since the last score update
        if current_time - self.last_update_time >= self.update_interval:
            self.score += random.randint(7, 12)
            self.update_score_text()  # Update the score text when the score changes
            self.last_update_time = current_time  # Reset the timer

    def draw(self, surface):
        # First, draw the score container image
        surface.blit(self.image, self.rect)

        # Render the score in the center of the container
        score_rect = self.score_num.get_rect(center=self.rect.center)
        score_rect.y -= 10
        surface.blit(self.score_num, score_rect)

    def get_final_score(self):

        final_score = self.score
        return final_score



class MuteButton (pygame.sprite.Sprite):
    def __init__(self):
        self.screen = GameContext.SCREEN

        self.audio_ON = pygame.image.load("data/assets/music/audio_enabled.png").convert_alpha()
        self.audio_OFF = pygame.image.load("data/assets/music/audio_muted.png").convert_alpha()

        self.audio_ON_rect = self.audio_ON.get_rect()
        self.audio_OFF_rect = self.audio_OFF.get_rect()
        
        self.audio_ON_rect.center = (GameContext.WIDTH - 35, 35)

    

    def update(self, mouse_pos):
        # Check if the mouse is clicking within the audio button's rectangle
        if self.audio_ON_rect.collidepoint(mouse_pos):
            # Toggle the audio state
            GameContext.AUDIO = not GameContext.AUDIO
            

    
    def draw(self, surface):
        if GameContext.AUDIO == True:
            surface.blit(self.audio_ON, self.audio_ON_rect)

        if GameContext.AUDIO == False:
            surface.blit(self.audio_OFF, self.audio_ON_rect)
        


class Paused(pygame.sprite.Sprite):
    def __init__(self):

        self.box = pygame.image.load("data/assets/ui/pause_overlay.png").convert_alpha()
        self.box.set_alpha(120) 
        self.box_rect = self.box.get_rect()
        self.box_rect.center = (GameContext.WIDTH/2, GameContext.HEIGHT/2)

        self.font = pygame.font.Font("data/fonts/open_serif_italic.ttf", 20)
        self.best_score = self.font.render(f"Best Score: {GameContext.HIGHEST_SCORE}", True, "#666666")
        self.best_score_rect = self.best_score.get_rect()
        self.best_score_rect.center = (GameContext.WIDTH/2, 220)

        self.unpause_prompt = self.font.render(f"Press Space to Unpause", True, "#666666")
        self.unpause_prompt_rect = self.unpause_prompt.get_rect()
        self.unpause_prompt_rect.center = (GameContext.WIDTH/2, 410)

        self.On = False


    def update(self):
        
        self.On = not self.On
        


    
    def draw(self, screen):
        

        screen.blit(self.box, self.box_rect)
        screen.blit(self.best_score, self.best_score_rect)
        screen.blit(self.unpause_prompt, self.unpause_prompt_rect)

class StartPrompt(pygame.sprite.Sprite):
    def __init__(self):
        self.start_prompt = pygame.image.load("data/assets/start_prompt.png").convert_alpha()
        self.start_prompt_rect = self.start_prompt.get_rect()
        self.start_prompt_rect.center = (GameContext.WIDTH/2, 250)


        self.transparency = 0
        self.start_prompt.set_alpha(self.transparency)
        self.visible = False
        
        self.timer = 0


    
    def update(self):

        if self.transparency >= 225:
            self.visible = True
        if self.transparency <= 0:
            self.visible = False


        self.timer += 1
        if self.timer >= 60 * 1.5:
            if self.timer % 1 == 0:
                
                if self.visible == False:
                    self.transparency += 4
                if self.visible == True:
                    self.transparency -= 2
        
        self.start_prompt.set_alpha(self.transparency)

        

        
    def draw(self, screen):

        screen.blit(self.start_prompt, self.start_prompt_rect)

class HighestScore(pygame.sprite.Sprite): 
    def __init__(self, height=165):

        
        self.font = pygame.font.Font("data/fonts/OpenSans-SemiboldItalic.ttf", 16)
        self.score = self.font.render(f"Best Score: {GameContext.HIGHEST_SCORE}", True, "#00B0E9")
        self.score.set_alpha(200)
        self.rect = self.score.get_rect()
        self.rect.center = (GameContext.WIDTH/2, height)


    def draw(self, screen):

        screen.blit(self.score, self.rect)

class Mascot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Initialize the sprite class
        self.y = 370  # Base Y position
        self.image = pygame.image.load("data/assets/ui/mascot2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (GameContext.WIDTH / 2, self.y)
        self.timer = 0

    def update(self):
        self.timer += 4  # Increment the timer to simulate time
        self.rect.y = sine_calculate(self.y, self.timer)  # Update y position based on sine wave

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # Draw the mascot on the screen


class YellowSpark(pygame.sprite.Sprite):
    def __init__(self):

        self.image = pygame.image.load("data/assets/ui/yellow_spark_1.png").convert_alpha()
        self.image2 = pygame.image.load("data/assets/ui/yellow_spark_2.png").convert_alpha()
        
        self.rect = self.image.get_rect()
        self.rect2 = self.image2.get_rect()

        self.rect.center = (GameContext.WIDTH/2, 325)
        

        self.state = True

        self.timer = 0
    
    def update(self):
        
        self.timer += 1

        if self.timer % 120 == 0:
            self.state = not self.state


    def draw(self, screen):

        if self.state:
            screen.blit(self.image, self.rect)
        else: screen.blit(self.image2, self.rect)
        


class WhiteSparkle(pygame.sprite.Sprite):
    def __init__(self, position=(70, 50), offset=0):
        
        super().__init__()
        self.original_image = pygame.image.load("data/assets/ui/white_sparkle.png").convert_alpha() #this is scaled oversize by 2
        self.image = self.original_image
       
        self.size = 0.5
        # self.image = pygame.transform.scale_by(self.image, 0.5 )
        
        self.rect = self.image.get_rect()
        self.rect.center = position

        self.timer = 0
        self.offset = offset       
        
    
    def update(self):
        
        self.timer += 1
        scale_factor = 0.5 + 0.2 * math.sin(0.045 * self.timer + self.offset)
        new_size = (int(self.original_image.get_width() * scale_factor), 
                    int(self.original_image.get_height() * scale_factor))
        self.image = pygame.transform.scale(self.original_image, new_size)
        self.rect = self.image.get_rect(center=self.rect.center)


    def draw(self, screen):

        screen.blit(self.image, self.rect)

class Backbutton(pygame.sprite.Sprite):
    def __init__(self):

        self.image = pygame.image.load("data/assets/ui/back_arrow.png")
        self.image_rect = self.image.get_rect()
        self.image_rect.topleft = (20, 15)

    

    def draw(self, screen):
        
        screen.blit(self.image, self.image_rect)


    def is_clicked(self, mouse_pos):
        # Check if the mouse position is within the button's rect
        return self.image_rect.collidepoint(mouse_pos)

class MainMenuButton(pygame.sprite.Sprite):
    def __init__(self):

        self.image = pygame.image.load("data/assets/ui/back_main_menu.png")
        self.image_rect = self.image.get_rect()
        self.image_rect.topleft = (20, 15)

    

    def draw(self, screen):
        
        screen.blit(self.image, self.image_rect)


    def is_clicked(self, mouse_pos):
        # Check if the mouse position is within the button's rect
        return self.image_rect.collidepoint(mouse_pos)

class TutorialIcon(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("data/assets/tutorial/tutorial_icon.png")
        self.image_rect = self.image.get_rect()
        self.image_rect.topleft = (320, 14)

    
    def draw(self, screen):
        
        screen.blit(self.image, self.image_rect)

    
    def is_clicked(self, mouse_pos):
        # Check if the mouse position is within the button's rect
        return self.image_rect.collidepoint(mouse_pos)

class PlayAgainPrompt(pygame.sprite.Sprite):
    def __init__(self):
        self.prompt = pygame.image.load("data/assets/play_again_prompt.png").convert_alpha()
        self.prompt_rect = self.prompt.get_rect()
        self.prompt_rect.center = (GameContext.WIDTH/2, GameContext.HEIGHT - 100)


        self.transparency = 0
        self.prompt.set_alpha(self.transparency)
        self.visible = False
        
        self.timer = 0


    
    def update(self):
        

        if self.transparency >= 225:
            self.visible = True
        if self.transparency <= 0:
            self.visible = False


        self.timer += 1
        if self.timer >= 60 * 1.5:
            if self.timer % 1 == 0:
                
                if self.visible == False:
                    self.transparency += 4
                if self.visible == True:
                    self.transparency -= 2
            
            self.prompt.set_alpha(self.transparency)

        

        
    def draw(self, screen):

        screen.blit(self.prompt, self.prompt_rect)

# Screens
class GameOver():
    def __init__(self, score=0):

        # Get score in text
        self.quip = quip_gen(score)

        self.reaction_sfx = studio_audience_sfx(score)

        
        self.screen = GameContext.SCREEN
        self.start_time = pygame.time.get_ticks()

        self.bg = pygame.Surface(self.screen.get_size())
        self.bg.fill((255, 255, 255))
        self.score_intro = pygame.image.load("data/assets/score_intro.png").convert_alpha()
        self.score_font = pygame.font.Font("data/fonts/OpenSans_Condensed-BoldItalic.ttf", 110)
        self.score_num = self.score_font.render(f"{score}", True, "#74A578")
        # self.prompt = pygame.image.load("data/assets/play_again_prompt.png").convert_alpha()
        self.prompt = PlayAgainPrompt()

        pygame.mixer.music.play(0)
        # self.reaction_sfx.play(0)

        # Get coordinates
        self.score_num_rect = self.score_num.get_rect()
        self.score_num_rect.center = (GameContext.WIDTH/2, 300)
        self.score_intro_rect = self.score_intro.get_rect()
        self.score_intro_rect.center = (GameContext.WIDTH/2, 100)
        # self.prompt_rect = self.prompt.get_rect()
        # self.prompt_rect.center = (GameContext.WIDTH/2, GameContext.HEIGHT - 100)
        self.quip_rect = self.quip.get_rect()
        self.quip_rect.center = (GameContext.WIDTH/2, GameContext.HEIGHT - 150)
        self.main_menu_nav = MainMenuButton()
        self.tutorial_icon = TutorialIcon()


        self.highest_score = HighestScore(585)




    def update(self, keys):
        self.current_time = pygame.time.get_ticks()
        
        
    
        if keys:  # Check if any key is pressed
            GameContext.GAME_OVER_VISITS += 1
            GameContext.PLAY_STATE = PlayStatus.GAMEPLAY


        if self.current_time - self.start_time >= 13000:  # 3000 milliseconds = 3 seconds
            GameContext.PLAY_STATE = PlayStatus.END_CREDITS

        

        

        self.prompt.update()
        
        
        

    def draw(self):
        # Method to draw on the screen
        
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.score_intro, self.score_intro_rect)
        self.screen.blit(self.score_num, self.score_num_rect)
        # self.screen.blit(self.prompt, self.prompt_rect)
        self.screen.blit(self.quip, self.quip_rect)
        self.prompt.draw(self.screen)
        self.main_menu_nav.draw(self.screen)
        self.tutorial_icon.draw(self.screen)
        self.highest_score.draw(self.screen)

class MainMenu:
    def __init__(self):

        GameContext.MAIN_MENU_VISITS += 1
    
        
        # GameContext.build_screen()
        self.screen = GameContext.SCREEN
        self.start_time = pygame.time.get_ticks()

        

        self.DTMG_logo = pygame.image.load("data/assets/ui/logo_without_shine.png")
        self.DTMG_logo_rect = self.DTMG_logo.get_rect()
        self.DTMG_logo_rect.center = (GameContext.WIDTH/2 +6, 100)
        self.background = pygame.image.load('./data/assets/background.png').convert_alpha()
        self.yellow_spark = YellowSpark()
        self.white_sparkle = WhiteSparkle()


        # self.start_prompt = pygame.image.load("data/assets/start_prompt.png").convert_alpha()
        # self.start_prompt_rect = self.start_prompt.get_rect()
        # self.start_prompt_rect.center = (GameContext.WIDTH/2, 250)


        # animated prompt
        self.start_prompt = StartPrompt()

        # highest score
        self.score = HighestScore()
        
        self.linkedin = LinkedIn()
        

        self.display_hands = pygame.image.load("data/assets/display_hands.png").convert_alpha()
        self.display_hands_rect = self.display_hands.get_rect()
        self.display_hands_rect.center = (GameContext.WIDTH/2, 429 + 211 / 2)

        self.mascot = Mascot()

        self.sparkle_cluster = pygame.sprite.Group(
            WhiteSparkle((79 + 5 ,43), 150),
            WhiteSparkle((72 + 5,61), 550),
            WhiteSparkle((90 + 5,59), 950)
        )


    def update(self, keys):
       
        self.yellow_spark.update()
        self.start_prompt.update()
        self.current_time = pygame.time.get_ticks()


        if GameContext.MAIN_MENU_VISITS >= 3:
             if self.current_time - self.start_time >= 1000:  
                if keys:  # Check if any key is pressed
                    GameContext.PLAY_STATE = PlayStatus.TUTORIAL

        # Check if 3 seconds have passed
        if self.current_time - self.start_time >= 2000:  
            if keys:  # Check if any key is pressed
                GameContext.PLAY_STATE = PlayStatus.TUTORIAL
        
        
        
        self.mascot.update()
        self.white_sparkle.update()

        self.sparkle_cluster.update()

    def draw(self):
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.DTMG_logo, self.DTMG_logo_rect)
        
        
        self.screen.blit(self.display_hands, self.display_hands_rect)
        
        self.start_prompt.draw(self.screen)
        
        self.score.draw(self.screen)

        self.mascot.draw(self.screen)

        self.yellow_spark.draw(self.screen)

        # self.white_sparkle.draw(self.screen)

        self.sparkle_cluster.draw(self.screen)
        self.linkedin.draw(self.screen)
        

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
        

        self.paused = False
        self.current_music_pos = 30
        

        

        

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
        
            keys = pygame.key.get_pressed()
        
                           

            # # if event.type == pygame.MOUSEBUTTONDOWN:
            # #     if event.button == 1:  # 1 is the left mouse button
            # #         mouse_pos = pygame.mouse.get_pos()

            # #     self.mute_button.update(mouse_pos)

                

                
            

            mouse_x, mouse_y = pygame.mouse.get_pos()
            

            

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
                    
                    GameContext.PLAY_STATE = PlayStatus.GAME_OVER
                    pygame.display.update()
                    return self.score_container.get_final_score()

            # Check for collisions with LeftHand
            for left_hand in self.left_hands:
                if self.check_collision(self.player, left_hand):
                   
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
            

class Tutorial:
    def __init__ (self):

        GameContext.TUTORIAL_VISITS += 1

        self.screen = GameContext.SCREEN
        self.start_time = pygame.time.get_ticks()


        self.tutorial_img = pygame.image.load("data/assets/tutorial/instructions screen.png")
        self.tutorial_img_rect = self.tutorial_img.get_rect()
        self.tutorial_img_rect.topleft = (0, 0)
        self.start_prompt = StartPrompt()
        self.start_prompt_img = self.start_prompt.start_prompt
        
        self.back_button = Backbutton()
        

    
    def update(self, keys):
        self.current_time = pygame.time.get_ticks()

        
        if keys:
            GameContext.PLAY_STATE = PlayStatus.GAMEPLAY


        if self.current_time - self.start_time >= 5000:
            self.start_prompt.update()


        

    
    def draw(self):

        
        self.screen.blit(self.tutorial_img, self.tutorial_img_rect)
        self.screen.blit(self.start_prompt_img, (50, 320))
        self.back_button.draw(self.screen)

        pygame.display.update()        

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

        self.image = pygame.image.load("data/assets/ui/credits_roll.png")
        self.image_rect = self.image.get_rect()
        self.pos = 1180  
        self.image_rect.center = (GameContext.WIDTH/2, self.pos)
        self.screen = GameContext.SCREEN
        self.bg_color = (102, 102, 102)
        self.clock = pygame.time.Clock()
        self.timer = 0


    def update(self):
        
        if self.pos == -200:
            self.timer += 1


        if self.timer >= 3000:
            GameContext.PLAY_STATE = PlayStatus.MAIN_MENU

        if self.pos > -185 - 20:
            self.pos -= 1
            self.image_rect.center = (GameContext.WIDTH/2, self.pos)
            self.clock.tick(60)
        
        


    def draw(self):

        self.screen.fill(self.bg_color)
        self.screen.blit(self.image, self.image_rect)

        pygame.display.update()

# Play States
async def credits_state():
    credits = Credits()

    while GameContext.PLAY_STATE == PlayStatus.CREDITS:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Update and draw the credits
        credits.update()
        credits.draw()

        # Update the screen
        pygame.display.flip()

        # Non-blocking sleep to maintain 60 FPS (1/60 seconds = 0.01667 seconds)
        await asyncio.sleep(0)
       

    # When exiting the loop, transition to the next state
    if GameContext.PLAY_STATE == PlayStatus.MAIN_MENU:
        await main_menu_state()

async def end_state():
    # end state logic
    pass

async def main_menu_state():
    main_menu = MainMenu()

    keys = False
    timer = 0

    while GameContext.PLAY_STATE == PlayStatus.MAIN_MENU:
        timer += 1
        
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if main_menu.linkedin.is_clicked(mouse_pos):
                        if __import__('sys').platform == "emscripten":
                           
                            js.window.open("https://www.linkedin.com/in/giovan-aaron-8410751b5/")

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if GameContext.MAIN_MENU_VISITS >= 3 and timer/60 >= 2:
                    keys = True

                elif timer / 60 >= 2:
                    keys = True

        main_menu.draw()
    
        main_menu.update(keys)

        pygame.display.flip()
        await asyncio.sleep(0)
    
    
        

async def gameplay_state():
    GameContext.build_screen()
    gameplay = Gameplay()
    paused = Paused()

    score = None  # Initialize score

    while GameContext.PLAY_STATE == PlayStatus.GAMEPLAY:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Toggle pause on spacebar press
                    paused.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 1 is the left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    gameplay.mute_button.update(mouse_pos)

                

        gameplay.draw()

        if paused.On:
            pygame.mixer.music.pause()
            paused.draw(GameContext.SCREEN)
            


        if not paused.On:
            pygame.mixer.music.unpause()
            score = gameplay.update()

        else:
            
            
            pygame.display.update()
            

        

        
        
        # score = gameplay.update()  # Ensure update returns the score

        pygame.display.flip()
        await asyncio.sleep(0)
    # Return the score when the game is over
    return score

async def game_over_state(score=0):
    if score > GameContext.HIGHEST_SCORE:
        GameContext.HIGHEST_SCORE = score
        
    game_over = GameOver(score)
    main_menu_nav = MainMenuButton()
    tutorial_icon = TutorialIcon()
    keys = False
    timer = 0

    while GameContext.PLAY_STATE == PlayStatus.GAME_OVER:
        timer += 1
        print(f"GAMEOVER visits:{GameContext.GAME_OVER_VISITS}")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if event.button == 1:  # Left mouse button
                        mouse_pos = pygame.mouse.get_pos()
                        
                        if main_menu_nav.is_clicked(mouse_pos):
                            
                            GameContext.PLAY_STATE = PlayStatus.MAIN_MENU

            if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if event.button == 1:  # Left mouse button
                        mouse_pos = pygame.mouse.get_pos()
                        
                        if tutorial_icon.is_clicked(mouse_pos):
                            
                            GameContext.PLAY_STATE = PlayStatus.TUTORIAL

            if event.type == pygame.KEYDOWN:
                if GameContext.GAME_OVER_VISITS >= 3 and timer/60 >= 1.5:
                    keys = True

                elif timer / 60 >= 3:
                    keys = True


        game_over.draw()
        game_over.update(keys)


        pygame.display.flip()
        await asyncio.sleep(0)

       


    # Handle transition back to the main menu or end
    if GameContext.PLAY_STATE == PlayStatus.MAIN_MENU:
        main_menu_state()
    elif GameContext.PLAY_STATE == PlayStatus.GAME_END:
        end_state()

async def tutorial_state():

    tutorial = Tutorial()
    back_button = Backbutton()
    keys = False
    timer = 0

    while GameContext.PLAY_STATE == PlayStatus.TUTORIAL:
        timer += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    
                    if back_button.is_clicked(mouse_pos):
                        
                        GameContext.PLAY_STATE = PlayStatus.MAIN_MENU
    
        
            if event.type == pygame.KEYDOWN:
                if GameContext.TUTORIAL_VISITS >= 2 and timer/60 >= 3:
                    keys = True
                elif timer / 60 >= 5:
                    keys = True

        tutorial.draw()
        tutorial.update(keys)
        
        pygame.display.flip()
        await asyncio.sleep(0)
    
    

       
        

async def end_credits_state():

    timer = 0

    end_credits = EndCredits()
    while GameContext.PLAY_STATE == PlayStatus.END_CREDITS:
        timer +=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if timer / 60 >= 4:
                    GameContext.PLAY_STATE = PlayStatus.MAIN_MENU

            if event.type == pygame.KEYDOWN:
                 if timer / 60 >= 4:
                    GameContext.PLAY_STATE = PlayStatus.MAIN_MENU



        
        end_credits.draw()
        end_credits.update()

        pygame.display.flip()
        await asyncio.sleep(0)

# Main
async def main():

    GameContext.PLAY_STATE = PlayStatus.CREDITS
    
    global GomeContext
    
    FPS = pygame.time.Clock()

    running = True
    while GameContext.PLAY_STATE:
          # Yield control to the event loop
        
        print("Current play state:", GameContext.PLAY_STATE)

        await asyncio.sleep(0) 
        
          
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        

        if GameContext.PLAY_STATE == PlayStatus.CREDITS:
            await credits_state()
            

        elif GameContext.PLAY_STATE == PlayStatus.MAIN_MENU:
            
            await main_menu_state()


        elif GameContext.PLAY_STATE == PlayStatus.TUTORIAL:
           
            await tutorial_state()

        elif GameContext.PLAY_STATE == PlayStatus.GAMEPLAY:
            
            score = await gameplay_state()  # Retrieve the score when gameplay ends

        elif GameContext.PLAY_STATE == PlayStatus.GAME_END:
            await end_state()


        elif GameContext.PLAY_STATE == PlayStatus.GAME_OVER:
            try:
                score
                await game_over_state(score)
            except: await game_over_state()  # Pass the score to the game over state

        elif GameContext.PLAY_STATE == PlayStatus.END_CREDITS:
            await end_credits_state()

        pygame.display.update()

        FPS.tick(60)
        pygame.time.wait(1000 // 60)

        


asyncio.run(main())