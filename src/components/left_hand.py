import pygame
import random
import math

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