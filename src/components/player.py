import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("data/assets/player_hand2.png").convert_alpha()  # Load the player's image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 6  # Speed at which the player moves

        self.mask = pygame.mask.from_surface(self.image)

         # Create an invisible cropped mask for collision detection
        self.collision_image = pygame.Surface((50, 50))  # Example size for the collision area
        self.collision_image.set_colorkey((0, 0, 255))  # Set transparency color
        self.collision_rect = self.collision_image.get_rect(center=self.rect.center)
        self.collision_mask = pygame.mask.from_surface(self.collision_image)

    def update(self, keys):
        # Move the player based on key presses
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        

        # Keep the player within the screen bounds
        self.rect.x = max(-50, min(self.rect.x, 575 - self.rect.width))
        self.rect.y = max(230, min(self.rect.y, 1000 - self.rect.height))

        self.collision_rect.center = self.rect.center

    def draw(self, surface):
        # Draw the player image
        surface.blit(self.image, self.rect)

        # Optionally, draw the collision mask for debugging
        if self.show_collision_mask:
            pygame.draw.rect(surface, (255, 0, 0), self.collision_rect, 2)  