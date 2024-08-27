import pygame

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

        self.collision_rect.x = self.rect.x + self.collision_buffer_x
        self.collision_rect.y = self.rect.y + self.collision_buffer_y

        # Keep the player within the screen bounds
        self.rect.x = max(-50, min(self.rect.x, 575 - self.rect.width))
        self.rect.y = max(230, min(self.rect.y, 1000 - self.rect.height))

        self.collision_rect.center = self.collision_rect.center

    def draw(self, surface):
        # Draw the player image
        surface.blit(self.image, self.rect)
        

        # Optionally, draw the collision mask for debugging
        # if self.show_collision_mask:
        #     pygame.draw.rect(surface, (255, 0, 0), self.collision_rect, 2)  