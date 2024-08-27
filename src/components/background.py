import pygame

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
