import pygame
from random import randint
BLACK = (0,0,0)
 
class Balle(pygame.sprite.Sprite):
    #This class represents a ball. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.vitesse = [randint(4,8),randint(-8,8)]
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.vitesse[0]
        self.rect.y += self.vitesse[1]
    
    def rebondVertical(self):
        self.vitesse[0] = -self.vitesse[0]
        self.vitesse[1] = randint(-8,8)
    
    def rebondHorizontal(self):
        self.vitesse[1] = -self.vitesse[1]
        self.vitesse[0] = randint(-8,8)