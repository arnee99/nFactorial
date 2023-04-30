import pygame
from config import *

# class Player(pygame.sprite.Sprite):
#     def __init__(self, game, x, y):
#         self.game = game
#         self._layer = PLAYER_LAYER
#         self.groups = self.game.all_sprites
#         pygame.sprite.Sprite.__init__(self, self.groups)
        
#         self.x = x * TILESIZE
#         self.y = y * TILESIZE
#         self.width = TILESIZE
#         self.height = TILESIZE
        
#         self.x_change = 0
#         self.y_change = 0
        
#         self.facing = 'down'
        
#         # image_to_load = pygame.image.load("images/frodo.png")
#         # self.image = pygame.Surface([self.width, self.height])
#         # self.image.set_colorkey(BLACK)
#         # self.image.blit(image_to_load, (0, 0))
#         self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
        
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y
        
#     def update(self):
#         self.movement()
        
#         self.rect.x += self.x_change
#         self.collide_blocks('x')
#         self.rect.y += self.y_change
#         self.collide_blocks('y')
        
#         self.x_change = 0
#         self.y_change = 0
    
#     def movement(self):
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT]:
#             self.x_change -= PLAYER_SPEED
#             self.facing = 'left'
#         if keys[pygame.K_RIGHT]:
#             self.x_change += PLAYER_SPEED
#             self.facing = 'right'
#         if keys[pygame.K_UP]:
#             self.y_change -= PLAYER_SPEED
#             self.facing = 'up'
#         if keys[pygame.K_DOWN]:
#             self.y_change += PLAYER_SPEED
#             self.facing = 'down'    
            
#     def collide_blocks(self, direction):
#         if direction == "x":
#             hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
#             if hits:
#                 if self.x_change > 0:
#                     self.rect.x = hits[0].rect.left - self.rect.width
#                 if self.x_change < 0:
#                     self.rect.x = hits[0].rect.right
        
#         if direction == "y":
#             hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
#             if hits:
#                 if self.y_change > 0:
#                     self.rect.y = hits[0].rect.top - self.rect.height
#                 if self.y_change < 0:
#                     self.rect.y = hits[0].rect.bottom
                    
class Fire(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.y_gravity = 1
        self.jump_height = 10
        self.y_velocity = self.jump_height
        
        self.x_change = 0
        self.y_change = 0
        
        self.facing = 'down'
        self.jumping = False
        
        # image_to_load = pygame.image.load("images/frodo.png")
        # self.image = pygame.Surface([self.width, self.height])
        # self.image.set_colorkey(BLACK)
        # self.image.blit(image_to_load, (0, 0))
        self.image = self.game.fire_spritesheet.get_sprite(0, 0, self.width, self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update(self):
        self.movement()
        
        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')
        
        self.x_change = 0
        self.y_change = 0
        
    # def jump(self):
        if self.jumping:
            self.y_change -= self.y_velocity
            self.y_velocity -= self.y_gravity
            if self.y_velocity < -self.jump_height:
                self.jumping = False
                self.y_velocity = self.jump_height
    
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_UP]:
            self.jumping = True
        if keys[pygame.K_DOWN]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'    
            
    def collide_blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
        
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
        
class Water(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.y_gravity = 1
        self.jump_height = 10
        self.y_velocity = self.jump_height
        
        self.x_change = 0
        self.y_change = 0
        
        self.facing = 'down'
        self.jumping = False
        
        # image_to_load = pygame.image.load("images/frodo.png")
        # self.image = pygame.Surface([self.width, self.height])
        # self.image.set_colorkey(BLACK)
        # self.image.blit(image_to_load, (0, 0))
        self.image = self.game.water_spritesheet.get_sprite(0, 0, self.width, self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update(self):
        self.movement()
        
        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')
        
        self.x_change = 0
        self.y_change = 0
        
        if self.jumping:
            self.y_change -= self.y_velocity
            self.y_velocity -= self.y_gravity
            if self.y_velocity < -self.jump_height:
                self.jumping = False
                self.y_velocity = self.jump_height  
    
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_d]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_w]:
            self.y_change -= PLAYER_SPEED
            self.jumping = True
        if keys[pygame.K_s]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'    
            
    def collide_blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
        
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom