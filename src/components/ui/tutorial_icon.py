import pygame

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
        

    
