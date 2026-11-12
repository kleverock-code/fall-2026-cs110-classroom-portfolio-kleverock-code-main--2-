import pygame
class Snowman(pygame.sprite.Sprite):
    def__init__(self,x,y, img="assests/snowman.png")
    super().__init__() #initalize sprite base class
    self.image = pygame.image.load(img) #surface
    self.rect = self.image.get_rect() #position and size
    self.rect.x = x
    self.rect.y = y