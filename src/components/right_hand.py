import pygame
import random
import math

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
        self.speed = random.randint(1, 6)
        self.direction = False  # True = left, False = right
        self.timer = 0
        self.soft_boundary_chance = 0.7  # Chance to respect soft boundaries

        # Parameters for sine wave movement
        self.amplitude = 50  # Amplitude of the sine wave
        self.frequency = 0.02  # Frequency of the sine wave
        self.original_x = x  # Store the original x position for sine calculation

    def update(self):
        self.timer += 4
        
        # Update speed every 60 frames
        if self.timer % 60 == 0:
            self.speed = random.randint(1, 6)

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
