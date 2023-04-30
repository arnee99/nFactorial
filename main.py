import pygame
import sys
from config import *
from sprites import *
from block import *
from player import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.background_image = pygame.image.load("images/background/wall2.png").convert()
        self.clock = pygame.time.Clock()
        self.running = True

        self.fire_spritesheet = Spritesheet("images/sprites/fire.png")
        self.water_spritesheet = Spritesheet("images/sprites/water.png")
        self.first_level_spritesheet = Spritesheet("images/background/jungle.jpeg")
        self.terrain_spritesheet = Spritesheet("images/sprites/terrain.png")
        

    # Function to draw a map
    def createTileMap(self):
        for i, row in enumerate(jungle_tilemap):
            for j, column in enumerate(row):
                if column == "W":
                    Block(self, j, i)
                if column == "F":
                    Fire(self, j, i)
                if column == "P":
                    Water(self, j, i)
                if column == "L":
                    Lava(self, j, i)
                if column == "C":
                    Ice(self, j, i)
                if column == "A":
                    Acid(self, j, i)
        
    # Function to handle events
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
    
    # Function to initialize a new game            
    def new(self):
        self.playing = True
        
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        
        self.createTileMap()
                
    # Function to update a game
    def update(self):
        self.all_sprites.update()

    # Function to draw each element
    def draw(self):
        # self.screen.blit(self.background_image, (0, 0))
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()
        
    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False
                
                

game = Game()
game.new()

while game.running:
    game.main()
    
pygame.quit()
exit()