import pygame
import random
import Projektil as pro 

# Die Elternklasse aller Gegner beinhaltet alle Funktionene, die alle Gegner gemeinsam haben
class Gegner(pygame.sprite.Sprite):
    
    # Alle Attribute werden instanziert
    def __init__(self, name, pos_x, pos_y, hp, mov_speed, img_paths, animation_speed, projectile_speed):
        self.name = name
        # Position auf dem Spielfeld
        self.pos_x = pos_x
        self.pos_y = pos_y
        # Hitpoints die die Gegner haben
        self.hp = hp
        # Geschwindigkeit der Gegner in X-Richtung
        self.speed = mov_speed
        # Geschwindigkeit der Gegner in Y-Richtung
        self.speed_y = 1
        # Der Pfad zu den Sprites
        self.img_paths = img_paths
        self.images = [[pygame.transform.scale(pygame.image.load(self.img_paths[i][0]).convert_alpha(), (80,80)) for i in range(len(self.img_paths))],[pygame.transform.scale(pygame.image.load(self.img_paths[i][1]).convert_alpha(), (80,80)) for i in range(len(self.img_paths))]]
        # Geschwindigkeit in der die Sprites ihr Aussehen ändern
        self.animation_speed = animation_speed
        self.animation_index = 0
        self.animation_index_2 = 0
        self.gegner_rect = self.images[0][0].get_rect(topleft=(self.pos_x,self.pos_y))
        # Liste aller Projektile des Gegners
        self.projektile = []
        # Cooldown der Attacken
        self.attack_ticker = 0
        # True = right, False = left
        self.direction = True
        # True = down, False = up
        self.direction_y = True
        self.check_y = False
        # Geschwindigkeit der Projektile
        self.projectile_speed = projectile_speed
    
    # Der Gegner bewegt sich in eine Richtung, bei Richtungsaenderung wird das Bild an der Y-Achse gespiegelt
    def movement(self):
        if self.gegner_rect.top <= 0:
            self.pos_y += self.speed_y
        if self.gegner_rect.top > 0:
            self.check_y = True
            if (random.randint(1,100) == 1):
                self.direction_y = not self.direction_y
            if self.direction_y:
                self.pos_y += self.speed_y
            else:
                self.pos_y -= self.speed_y
         
        if (random.randint(1,100) == 1):
            self.direction = not self.direction
        if self.direction:
            self.pos_x += self.speed
        else:
            self.pos_x -= self.speed
        
    
    # Der Gegner schießt ein Projektil in Richtung des Spielers 
    def generate_projektil(self):
        if self.attack_ticker == 0:
            if self.name == 'Quak':
                self.projektile.append(pro.Projektil_bread(self.pos_x + (self.gegner_rect.width / 2), self.pos_y, self.projectile_speed))
            elif self.name == 'Ghost':
                self.projektile.append(pro.Projektil_ghost(self.pos_x + (self.gegner_rect.width / 2), self.pos_y, self.projectile_speed))
            elif self.name == 'Blume':
                self.projektile.append(pro.Projektil_seed(self.pos_x + (self.gegner_rect.width / 2), self.pos_y, self.projectile_speed))
            elif self.name == 'Rock':
                self.projektile.append(pro.Projektil_rock(self.pos_x + (self.gegner_rect.width / 2), self.pos_y, self.projectile_speed))
            elif self.name == 'Stift':
                self.projektile.append(pro.Projektil_pencil(self.pos_x + (self.gegner_rect.width / 2), self.pos_y, self.projectile_speed))

        self.attack_ticker += 1
        if self.attack_ticker >= 100:
            self.attack_ticker = 0
    
    # Es wird geprueft, das der Gegner innerhalb des Spielfeldes bleibt
    # Beruehrt ein Gegner eine Spielfeldwand, wird seine Bewegungsrichtung automatisch geaendert
    def check_game_border(self, width, height):
        if self.pos_x < 0:
            self.pos_x = 0
            self.direction = True
        if self.gegner_rect.right > width:
            self.pos_x = width - self.gegner_rect.width
            self.direction = False
        
        if self.check_y == True:
            if self.gegner_rect.top < 0:
                self.pos_y = 0
                self.direction_y = True
            if self.gegner_rect.bottom > int(height / 2):
                self.pos_y = int(height / 2) - self.gegner_rect.height
                self.direction_y = False

    # update sorgt dafuer, dass die Koordinaten von Rect und Surface aktuell sind
    def update(self):
        self.gegner_rect = self.images[0][0].get_rect(topleft=(self.pos_x,self.pos_y))
        if self.animation_index < (len(self.images) - 1):
            self.animation_index += self.animation_speed
        else:
            self.animation_index = 0
    
    # Hat der Gegner 0 Leben, wird er und seine Projektile von dem Spielfeld entfernt
    def ist_tot(self):
        if self.hp <= 0:
            for projektil in self.projektile:
                self.projektile.remove(projektil)
            return True
        else:
            return False
            

# Alle Gegner erben von der Gegnerklasse, die Parameter sind:
# Name, X-Position, Y-Position, Leben, Geschwindigkeit, Pfad zum Bild, Projektilgeschwindigkeit
class Gegner_quak(Gegner):   
    def __init__(self, pos_x, pos_y, projectile_speed):
        super().__init__('Quak', pos_x, pos_y, 10, 3, [['Sprites_new/Quack_1.png','Sprites_new/Quack_2.png'], ['Sprites_new/quack_angry_1.png','Sprites_new/quack_angry_2.png']], 0.05, projectile_speed)
    def update(self):
        self.gegner_rect = self.images[0][0].get_rect(topleft=(self.pos_x,self.pos_y))
        if self.animation_index < (len(self.images) - 1):
            self.animation_index += self.animation_speed
        else:
            self.animation_index = 0
        if self.hp < 5:
            self.animation_index_2 = 1
            self.speed = 5
class Gegner_ghost(Gegner):   
    def __init__(self, pos_x, pos_y, projectile_speed):
        super().__init__('Ghost', pos_x, pos_y, 5, 5, [['Sprites_new/Ghost_1.png', 'Sprites_new/Ghost_2.png']], 0.01, projectile_speed)
        #self.shadow.fill('white')
class Gegner_stift(Gegner):   
    def __init__(self, pos_x, pos_y, projectile_speed):
        super().__init__('Stift', pos_x, pos_y, 7, 2, [['Sprites_new/Stift_1.png', 'Sprites_new/Stift_2.png']], 0.05, projectile_speed)
class Gegner_rock(Gegner):   
    def __init__(self, pos_x, pos_y):
        super().__init__('Rock', pos_x, pos_y, 20, 0, [['Sprites/rock.png', 'Sprites/rock_fractured.png']], 0.05, 0)
    def update(self):
        if self.hp < 7:
            self.animation_index = 1
    def movement(self):
        pass
    def generate_projektil(self):
        pass
class Gegner_blume(Gegner):
   def __init__(self, pos_x, pos_y, projectile_speed):
        super().__init__('Blume', pos_x, pos_y, 10, 2, [['Sprites_new/Blume_1.png', 'Sprites_new/Blume_2.png']], 0.02, projectile_speed)
        



 

    
    

