import pygame
import random
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

