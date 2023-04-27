import pygame
from config import *

class Map:
    def __init__(self, image):
        self.background = pygame.image.load(image)
        
    