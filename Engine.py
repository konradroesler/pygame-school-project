import pygame
import random
import Gegner as geg
import Screen as scr
import Spieler as pla
import Regulator as reg
import random

# Engine beinhaltet die wichtigen Instanzen der Objekte wie den Spieler oder den Screen.
# Es wird nur eine Instanz der Klasse Engine erstellt, 
# mit der ueber die Haupt-While-Schleife das gesamte Spielgeschehen gesteuert wird. 
class Engine:

    # Alle relevanten Klassen werden instanziert 
    def __init__(self):
        self.running = False
        self.score = 0
        self.scoreTicker = 0
        self.runtime = 0
        self.tries = 0
        self.enemy_multiplier = 1
        self.enemy_projectile_speed = 7
        self.screen = scr.Screen()
        self.spieler = pla.Player(int(self.screen.display.get_width() / 3), int(7 * self.screen.display.get_width() / 8))
        self.gegner = []
        # Musik
        self.music_paused = False
        self.just_clicked = False
        self.music_volume = 50
        self.music_name_list = ['track_1','track_2','track_3','track_4','track_5','track_6','track_7','track_8']
        random.shuffle(self.music_name_list)
        self.playlist = ['Music/' + i + '.mp3' for i in self.music_name_list]
        pygame.mixer.music.load(self.playlist[0])
        self.playlist.append(self.playlist[0])
        self.playlist.pop(0)
        pygame.mixer.music.play()
        pygame.mixer.music.queue(self.playlist[0])
        self.playlist.append(self.playlist[0])
        self.playlist.pop(0)
        self.MUSIC_END = pygame.USEREVENT+1
        self.MUSIC_END_EVENT = pygame.event.Event(self.MUSIC_END)
        pygame.mixer.music.set_endevent(self.MUSIC_END)
        
    def check_input(self):
        # Input fuer den Spieler
        # "keys" ist eine Liste aller runtergedrückten Tasten
        keys  = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.spieler.mov_up()
        if keys[pygame.K_s]:
            self.spieler.mov_down()
        if keys[pygame.K_d]:
            self.spieler.mov_right()
        if keys[pygame.K_a]:
            self.spieler.mov_left()
        if keys[pygame.K_k]:
            if self.spieler.attack_ticker == 0:
                self.spieler.generate_projektil()
            self.spieler.attack_ticker += 1
    
    # Ein Gegner wird zufaellig erstellt 
    def generate_enemy(self):
        value = random.randint(1,5)
        if value == 1:
            new_geg = geg.Gegner_quak(random.randint(0, int(2 * self.screen.display.get_width() / 3) - 50),-100, self.enemy_projectile_speed)
            self.gegner.append(new_geg)
        elif value == 2:
            new_geg = geg.Gegner_ghost(random.randint(0, int(2 * self.screen.display.get_width() / 3) - 50),-100, self.enemy_projectile_speed)
            self.gegner.append(new_geg)
        elif value == 3:
            new_geg = geg.Gegner_stift(random.randint(0, int(2 * self.screen.display.get_width() / 3) - 50),-100, self.enemy_projectile_speed)
            self.gegner.append(new_geg)
        elif value == 4:
            new_geg = geg.Gegner_rock(random.randint(0, int(2 * self.screen.display.get_width() / 3) - 50), random.randint(int(self.screen.display.get_height() / 3), int(2 * self.screen.display.get_height() / 3)))
            self.gegner.append(new_geg)
        elif value == 5:
            new_geg = geg.Gegner_blume(random.randint(0, int(2 * self.screen.display.get_width() / 3) - 50), -100, self.enemy_projectile_speed)
            self.gegner.append(new_geg)

    # Es wird die Kollision aller Spielerprojektile mit den Gegnern und alle Gegnerprojektile mit dem Spieler geprueft
    def projektil_collision(self):
        # Projektile des Spielers Kollision mit Gegnern 
        for projektil in self.spieler.projektile:
            for gegner in self.gegner:
                if pygame.Rect.colliderect(projektil.projektil_rect, gegner.gegner_rect) == True and projektil in self.spieler.projektile:
                    # Projektil wird geloescht und Leben von dem Gegner um eins reduziert
                    self.spieler.projektile.remove(projektil)
                    gegner.hp -= 1
        for gegner in self.gegner:
            for projektil in gegner.projektile:
                if pygame.Rect.colliderect(projektil.projektil_rect, self.spieler.rect) == True and projektil in gegner.projektile:
                    gegner.projektile.remove(projektil)
                    self.spieler.hp -= 1
                for gegner_rock in self.gegner:
                    if gegner_rock.name == 'Rock':
                        if pygame.Rect.colliderect(projektil.projektil_rect, gegner_rock.gegner_rect) == True and projektil in gegner.projektile:
                            gegner.projektile.remove(projektil)
                            gegner_rock.hp -= 1
                    
    def rock_collision(self):
        for gegner in self.gegner:
            if (self.spieler.rect.colliderect(gegner.gegner_rect) and gegner.name == 'Rock'):
                center_rock = gegner.gegner_rect.center
                center_spieler = self.spieler.rect.center
                distance_x = center_rock[0] - center_spieler[0]
                distance_y = center_rock[1] - center_spieler[1]
                if abs(distance_x) < abs(distance_y):
                    if distance_y > 0:
                        self.spieler.pos_y = gegner.gegner_rect.top - self.spieler.rect.height
                    elif distance_y < 0:
                        self.spieler.pos_y = gegner.gegner_rect.bottom 
                elif abs(distance_x) > abs(distance_y):
                    if distance_x < 0:
                        self.spieler.pos_x = gegner.gegner_rect.right
                    elif distance_x > 0:
                        self.spieler.pos_x = gegner.gegner_rect.left - self.spieler.rect.width + 10 
    
    # Methode um den Score des Spielers zu aktualisieren
    def updateScore(self):
        self.scoreTicker += 1
        if self.scoreTicker % 60 == 0:
            self.score += 10
            
    def movement(self):
        # Gegner und Projektiele Bewegen sich
        for projektil in self.spieler.projektile:
            projektil.movement_spieler()
        for gegner in self.gegner:
            gegner.movement()
            gegner.update()
            for projektil in gegner.projektile:
                projektil.movement_gegner()   
    
    def collisions(self):
        # Alle Kollisionen von Spieler, Gegnern und Projektilen
        self.spieler.check_game_border(int(2 * self.screen.display.get_width() / 3), self.screen.display.get_height())
        self.rock_collision()
        for gegner in self.gegner:
            gegner.check_game_border(int(2 * self.screen.display.get_width() / 3), self.screen.display.get_height())
        self.projektil_collision()
    
    def deletions(self):
        # Wenn etwas aus dem Spielfeld entfernt werden soll, dann hier
        for projektil in self.spieler.projektile:
            if projektil.ist_weg() == True:
                self.spieler.projektile.remove(projektil)
        for gegner in self.gegner:
            if gegner.ist_tot() == True:
                self.gegner.remove(gegner)
                self.score += 100
            for projektil in gegner.projektile:
                if projektil.ist_weg() == True:
                    gegner.projektile.remove(projektil)
                    
    def draw_statics(self):
        # Alle statischen Objekte werden gezeichnet
        self.screen.update()
        self.screen.render_text(f'Score: {int(self.score)}', int(self.screen.display.get_height() / 20), int(2.1 * self.screen.display.get_width() / 3), int(0.5 * self.screen.display.get_height() / 10), (255,255,255))
        self.screen.render_text(f'Health: {self.spieler.hp}', int(self.screen.display.get_height() / 20), int(2.1 * self.screen.display.get_width() / 3), int(1 * self.screen.display.get_height() / 10), (255,255,255))
        self.screen.render_text(f'Time: {int(self.runtime)}', int(self.screen.display.get_height() / 20), int(2.1 * self.screen.display.get_width() / 3), int(1.5 * self.screen.display.get_height() / 10), (255,255,255))
        self.screen.render_text(f'Try: {int(self.tries)}', int(self.screen.display.get_height() / 20), int(2.1 * self.screen.display.get_width() / 3), int(2 * self.screen.display.get_height() / 10), (255,255,255))
        # regulators
        self.screen.draw_regulator(self.screen.player_speed_regulator, self.spieler.mov_speed)
        self.screen.draw_regulator(self.screen.enemy_multiplier_regulator, self.enemy_multiplier)
        self.screen.draw_regulator(self.screen.player_attack_multiplier_regulator, self.spieler.attack_ticker_multiplier)
        self.screen.draw_regulator(self.screen.player_projectile_speed_regulator, self.spieler.projectile_speed)
        self.screen.draw_regulator(self.screen.enemy_projectile_speed_regulator, self.enemy_projectile_speed)
        # ambiante
        for e in self.screen.bush_cords:
            self.screen.blit(self.screen.bush_img, e[0], e[1])
        # music manager 
        self.screen.draw_music_manager(self.screen.music_manager, self.music_volume, self.music_paused)
        if self.running == False and self.tries == 0:
            pygame.draw.rect(self.screen.display, (255,255,255), self.screen.start_game_rect)
            self.screen.blit(self.screen.start_game, int(self.screen.game_screen.width/2 - self.screen.start_game_rect.width/2), int(self.screen.game_screen.height/2 - self.screen.start_game_rect.height/2))
        if self.running == False and self.tries > 0:
            pygame.draw.rect(self.screen.display, (255,255,255), self.screen.retry_game_rect)
            self.screen.blit(self.screen.retry_game, int(self.screen.game_screen.width/2 - self.screen.retry_game_rect.width/2), int(self.screen.game_screen.height/2 - self.screen.retry_game_rect.height/2))
        if self.running == True:
            pygame.draw.rect(self.screen.display, (30,30,30), self.screen.exit_game_rect)
            self.screen.blit(self.screen.exit_game, int(2.1 * self.screen.display.get_width() / 3), int(9 * self.screen.display.get_height() / 10))

        
    def draw_dynamics(self):
        # Alle spieler/gegner werden gezeichnet
        self.screen.blit(self.spieler.image, self.spieler.pos_x, self.spieler.pos_y)
        for gegner in self.gegner:
            if gegner.direction:
                self.screen.blit(gegner.images[round(gegner.animation_index)][gegner.animation_index_2], gegner.pos_x, gegner.pos_y)
            elif not gegner.direction:
                self.screen.blit(pygame.transform.flip(gegner.images[round(gegner.animation_index)][gegner.animation_index_2], True, False), gegner.pos_x, gegner.pos_y)
            for projektil in gegner.projektile:
                self.screen.blit(projektil.image, projektil.pos_x, projektil.pos_y)
        for projektil in self.spieler.projektile:
            self.screen.blit(projektil.image, projektil.pos_x, projektil.pos_y)    
    
    def player_ded(self):
        # pruefen, ob der Spieler keine Leben mehr hat
        if self.spieler.ist_tot():
            self.running = False
            for gegner in self.gegner:
                self.gegner.remove(gegner)
    
    def generate_stuff(self):
        # Generiere Gegner/Projektiele der Gegner
        if random.randint(1,int(200/(self.enemy_multiplier/2))) == 1:
            self.generate_enemy()
        for gegner in self.gegner:
            gegner.generate_projektil()

    def restart(self):
        self.running = True
        self.spieler.hp = 5
        self.score = 0
        self.runtime = 0
        self.tries += 1
        self.spieler.pos_x = self.spieler.start_x
        self.spieler.pos_y = self.spieler.start_y
        self.spieler.projektile = []

    # run uebernimmt gemeinsam mit der Haupt-While-Schleife den Spielablauf. 
    def run(self):
        if self.running:
            self.runtime += 1/60
            self.updateScore()
            self.generate_stuff()
            self.check_input()
            self.spieler.update()
            self.movement()
            self.collisions()
            self.deletions()
        self.draw_statics()
        if self.running:
            self.draw_dynamics()
        self.player_ded()
        self.just_clicked = False
        # WICHTIG >> muss abschliessend verwendet werden, damit ALLE Elemente auf dem Bildschirm dargestellt werden.
        pygame.display.flip()

