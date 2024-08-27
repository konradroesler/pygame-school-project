import pygame
import Projektil as pro 

# Der Spieler wird von dem Benutzer gesteuert und wird nur ein Mal in der Engine Klasse instanziert
class Player(pygame.sprite.Sprite):
    
    # Der Spieler wird konstruiert
    def __init__(self,start_x,start_y):
        super().__init__()
        self.hp = 5
        self.mov_speed = 10
        self.start_x = start_x - 25
        self.start_y = start_y - 25
        self.pos_x = start_x
        self.pos_y = start_y
        self.image = pygame.transform.scale(pygame.image.load('Sprites/spieler.png').convert_alpha(), (50,50))
        self.rect = self.image.get_rect(topleft=(self.pos_x - 10,self.pos_y))
        self.projektile = []
        self.attack_ticker = 0
        self.max_ticker = 10
        self.attack_ticker_multiplier = 1
        self.projectile_speed = 12
   
    def mov_right(self):
        self.pos_x = self.pos_x + self.mov_speed
    def mov_left(self):
        self.pos_x = self.pos_x - self.mov_speed
    def mov_up(self):
        self.pos_y = self.pos_y - self.mov_speed
    def mov_down(self):
        self.pos_y = self.pos_y + self.mov_speed
    # Wird die Taste j vom Spieler gedrueckt, fokussiert dieser und wird langsamer 
    def focus_enable(self):
        self.mov_speed = int(self.mov_speed / 2)
    def focus_disable(self):
        self.mov_speed = int(self.mov_speed * 2)
    def set_mov_speed(self, mov_speed):
        self.mov_speed = mov_speed
    
    # Drueckt der Spieler k wird ein Projektil generiert 
    def generate_projektil(self):
        self.projektile.append(pro.Projektil_spieler(self.pos_x + int(self.rect.width / 2) - 5, self.pos_y - 5, self.projectile_speed)) 
    
    # Es wird geprueft, ob sich der Spieler innerhalb der des Spielfeldes befindet
    def check_game_border(self, width, height):
        if self.pos_y < 0:
            self.pos_y = 0
        if self.pos_x < 0:
            self.pos_x = 0
        if self.rect.bottom > height:
            self.pos_y = height - self.rect.height
        if self.rect.right + 10 > width:
            self.pos_x = width - self.rect.width
        
    def ist_tot(self):
        if self.hp <= 0:
            return True
    
    # update sorgt dafuer, dass die Koordinaten von Rect und Surface aktuell sind
    def update(self):
        self.rect = self.image.get_rect(topleft=(self.pos_x - 10,self.pos_y))
        if self.attack_ticker >= int(self.max_ticker - self.attack_ticker_multiplier):
            self.attack_ticker = 0
            

