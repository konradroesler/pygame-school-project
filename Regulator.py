import pygame 

class Regulator:
    def __init__(self, root_x, root_y, text):
        self.root_x = root_x
        self.root_y = root_y
        # Text section
        self.text = text
        self.text_x = self.root_x
        self.text_y = self.root_y - 15
        # Plus
        self.plus_x = self.root_x + 80
        self.plus_y = self.root_y + 15
        self.plus_img = pygame.transform.scale(pygame.image.load('Sprites_new/Regulator_plus.png').convert_alpha(), (40,40))
        self.plus_rect = pygame.Rect(0,0,40,40)
        self.plus_rect.topleft = (self.plus_x, self.plus_y)
        # Minus
        self.minus_x = self.root_x 
        self.minus_y = self.root_y + 15
        self.minus_img = pygame.transform.scale(pygame.image.load('Sprites_new/Regulator_minus.png').convert_alpha(), (40,40))
        self.minus_rect = pygame.Rect(0,0,40,40)
        self.minus_rect.topleft = (self.minus_x, self.minus_y)
        
class Regulator_music:
    def __init__(self, root_x, root_y, text):
        self.root_x = root_x
        self.root_y = root_y
        # Text section
        self.text = text
        self.text_x = self.root_x - 8
        self.text_y = self.root_y - 15
        # Plus
        self.plus_x = self.root_x + 30
        self.plus_y = self.root_y + 15
        self.plus_img = pygame.transform.scale(pygame.image.load('Sprites_new/Regulator_plus.png').convert_alpha(), (30,30))
        self.plus_rect = pygame.Rect(0,0,30,30)
        self.plus_rect.topleft = (self.plus_x, self.plus_y)
        # Minus
        self.minus_x = self.root_x 
        self.minus_y = self.root_y + 15
        self.minus_img = pygame.transform.scale(pygame.image.load('Sprites_new/Regulator_minus.png').convert_alpha(), (30,30))
        self.minus_rect = pygame.Rect(0,0,30,30)
        self.minus_rect.topleft = (self.minus_x, self.minus_y)
        # Pause/Unpause
        self.pause_x = self.root_x - 30
        self.pause_y = self.root_y + 15
        self.pause_img = pygame.transform.scale(pygame.image.load('Sprites_new/Pause_button.png').convert_alpha(), (30,30))
        self.pause_rect = pygame.Rect(0,0,30,30)
        self.pause_rect.topleft = (self.pause_x, self.pause_y)
        self.unpause_img = pygame.transform.scale(pygame.image.load('Sprites_new/Unpause_button.png').convert_alpha(), (30,30))
        self.unpause_rect = pygame.Rect(0,0,30,30)
        self.unpause_rect.topleft = (self.pause_x, self.pause_y)
        # Skip
        self.skip_x = self.root_x + 60
        self.skip_y = self.root_y + 15
        self.skip_img = pygame.transform.scale(pygame.image.load('Sprites_new/Skip_button.png').convert_alpha(), (30,30))
        self.skip_rect = pygame.Rect(0,0,30,30)
        self.skip_rect.topleft = (self.skip_x, self.skip_y)