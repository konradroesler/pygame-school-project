import pygame

# Die Projektilklasse ist das Baugeruest fuer alle Projektile 
class Projektil:

    # Die Klasse wird initialisiert 
    def __init__(self, pos_x, pos_y, img_path, mov_speed, projectile_size):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = mov_speed
        self.image = pygame.transform.scale(pygame.image.load(img_path).convert_alpha(), projectile_size)
        self.projektil_rect = self.image.get_rect(center=(self.pos_x,self.pos_y))
    
    # Die Projektile bewegen sich mit konstanter Geschwindkeit in eine Richtung
    # Für den Spieler nach oben
    def movement_spieler(self):
        self.pos_y -= self.speed
        self.projektil_rect = self.image.get_rect(center=(self.pos_x,self.pos_y))
    # Für den Gegner nach unten
    def movement_gegner(self):
        self.pos_y += self.speed
        self.projektil_rect = self.image.get_rect(center=(self.pos_x,self.pos_y))
    
    # Verlaesst das Projektil das Spielfeld, wird dieses entfernt
    def ist_weg(self):
        if self.pos_y < (-200) or self.pos_y > 1200:
            return True
        else:
            return False

# Alle Projektile erben von der Projektilklasse, die Parameter sind:
# X-Position, Y-Position, Pfad zum Image, Geschwindigkeit, Groesse
class Projektil_spieler(Projektil):
 def __init__(self, pos_x, pos_y, speed):
        super().__init__(pos_x, pos_y, 'Sprites_new/laser.png', speed, (10,30))  
        self.image = pygame.transform.flip(self.image, False, True)
class Projektil_messer(Projektil):
 def __init__(self, pos_x, pos_y, speed):
        super().__init__(pos_x, pos_y, 'Sprites/messer.png', speed, (30,30))  
class Projektil_rock(Projektil):
 def __init__(self, pos_x, pos_y, speed):
        super().__init__(pos_x, pos_y, 'Sprites/rock.png', speed,(30,30))  
class Projektil_bread(Projektil):
 def __init__(self, pos_x, pos_y, speed):
        super().__init__(pos_x, pos_y, 'Sprites_new/Bread.png', speed, (30,30))
class Projektil_ghost(Projektil):
 def __init__(self, pos_x, pos_y, speed):
        super().__init__(pos_x, pos_y, 'Sprites_new/Ghost_projectile.png', speed, (30,40))
class Projektil_seed(Projektil):
 def __init__(self, pos_x, pos_y, speed):
        super().__init__(pos_x, pos_y, 'Sprites_new/Seed.png', speed, (25,30))
class Projektil_pencil(Projektil):
 def __init__(self, pos_x, pos_y, speed):
        super().__init__(pos_x, pos_y, 'Sprites_new/Pencil_tip.png', speed, (10,30))