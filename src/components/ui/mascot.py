import pygame
from game_context import GameContext
from src.utils.sine_calculator import sine_calculate

class Mascot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Initialize the sprite class
        self.y = 370  # Base Y position
        self.image = pygame.image.load("data/assets/ui/mascot2.png")
        self.rect = self.image.get_rect()
        self.rect.center = (GameContext.WIDTH / 2, self.y)
        self.timer = 0

    def update(self):
        self.timer += 4  # Increment the timer to simulate time
        self.rect.y = sine_calculate(self.y, self.timer)  # Update y position based on sine wave

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # Draw the mascot on the screen
