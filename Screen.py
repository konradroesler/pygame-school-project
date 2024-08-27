import pygame
import random
import Regulator as reg

# Screen beinhalted alle Funktion die der Darstellung der Funktionen des Spiels dienen
# Es wird nur eine Instanz der Klasse Scree, unzwar der einzigen Instanz der Klasse Engine erstellt 
class Screen:

    # Hier werden alle statischen Bildelemente als von Pygame bereits 'Surface' Objekte initialisiert
    def __init__(self): 
        # self.display ist der 'Displaysurface' also das Fenster auf dem alles abgebildet wird
        self.display = pygame.display.set_mode((800,800), pygame.RESIZABLE)
        self.game_screen = pygame.draw.rect(self.display, (0,0,0), pygame.Rect(0,0,int(2 * self.display.get_width() / 3),int(self.display.get_height())))
        self.stat_screen = pygame.draw.rect(self.display, (30,30,30), pygame.Rect(int(2 * self.display.get_width() / 3),0,int(self.display.get_width() / 3),int(self.display.get_height())))
        self.enemy_rect = pygame.draw.rect(self.display, (0,0,0), pygame.Rect(0,0,int(2 * self.display.get_width() / 3),int(self.display.get_height() / 2)))
        self.start_game = pygame.transform.scale(pygame.image.load('Sprites/start_game.png').convert_alpha(), (200,100))
        self.start_game_rect = pygame.draw.rect(self.display, (0,0,0), pygame.Rect(0,0,200,100))
        self.start_game_rect.center = (int(self.game_screen.width/2),int(self.game_screen.height/2))
        self.retry_game = pygame.transform.scale(pygame.image.load('Sprites/play_again.png').convert_alpha(), (200,100))
        self.retry_game_rect = pygame.draw.rect(self.display, (0,0,0), pygame.Rect(0,0,200,100))
        self.retry_game_rect.center = (int(self.game_screen.width/2),int(self.game_screen.height/2))
        self.exit_game = pygame.transform.scale(pygame.image.load('Sprites_new/Exit_button.png').convert_alpha(), (100,50))
        self.exit_game_rect = pygame.draw.rect(self.display, (0,0,0), pygame.Rect(int(2.1 * self.display.get_width() / 3), int(9 * self.display.get_height() / 10),100,50)) 
        self.background = pygame.transform.scale(pygame.image.load('Sprites_new/Meadow.png').convert_alpha(), (1920,1080))
        # regulators
        self.player_speed_regulator = reg.Regulator(int(2.1 * self.display.get_width() / 3), int(3 * self.display.get_height() / 10), 'Player Speed')
        self.enemy_multiplier_regulator = reg.Regulator(int(2.1 * self.display.get_width() / 3), int(4 * self.display.get_height() / 10), 'Enemy Multiplier')
        self.player_attack_multiplier_regulator = reg.Regulator(int(2.1 * self.display.get_width() / 3), int(5 * self.display.get_height() / 10), 'Player Attack Multiplier')
        self.player_projectile_speed_regulator = reg.Regulator(int(2.1 * self.display.get_width() / 3), int(6 * self.display.get_height() / 10), 'Player Projectile Speed')
        self.enemy_projectile_speed_regulator = reg.Regulator(int(2.1 * self.display.get_width() / 3), int(7 * self.display.get_height() / 10), 'Enemy Projectile Speed')
        # music
        self.music_manager = reg.Regulator_music(int(2.6 * self.display.get_width() / 3) + 5, int(9 * self.display.get_height() / 10), 'Music')
        # ambiante
        self.bush_img = pygame.transform.scale(pygame.image.load('Sprites_new/bush_1.png').convert_alpha(), (30,30))
        self.bush_cords = [(random.randint(20,self.game_screen.width-20),random.randint(20,self.game_screen.height-20)) for i in range(random.randint(5,8))]
        
        
    # Wird die Groesse des Fensters veraendert, werden die statischen Bildelemente einmalig neu erstellt
    def set_display_size(self, width, height):
        self.display = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        self.game_screen = pygame.draw.rect(self.display, (0,0,0), pygame.Rect(0,0,int(2 * self.display.get_width() / 3),int(self.display.get_height())))
        self.stat_screen = pygame.draw.rect(self.display, (30,30,30), pygame.Rect(int(2 * self.display.get_width() / 3),0,int(self.display.get_width() / 3),int(self.display.get_height())))
        self.enemy_rect = pygame.draw.rect(self.display, (0,0,0), pygame.Rect(0,0,int(2 * self.display.get_width() / 3),int(self.display.get_height() / 2)))
        self.start_game_rect = pygame.draw.rect(self.display, (0,0,0), pygame.Rect(0,0,200,100))
        self.start_game_rect.center = (int(self.game_screen.width/2),int(self.game_screen.height/2))
        self.retry_game = pygame.transform.scale(pygame.image.load('Sprites/play_again.png').convert_alpha(), (200,100))
        self.retry_game_rect = pygame.draw.rect(self.display, (0,0,0), pygame.Rect(0,0,200,100))
        self.retry_game_rect.center = (int(self.game_screen.width/2),int(self.game_screen.height/2))
        self.retry_game_rect.center = (int(self.game_screen.width/2),int(self.game_screen.height/2))
        self.exit_game = pygame.transform.scale(pygame.image.load('Sprites_new/Exit_button.png').convert_alpha(), (100,50))
        self.exit_game_rect = pygame.draw.rect(self.display, (0,0,0), pygame.Rect(int(2.1 * self.display.get_width() / 3), int(9 * self.display.get_height() / 10),100,50))
        self.background = pygame.transform.scale(pygame.image.load('Sprites_new/Meadow.png').convert_alpha(), (1920,1080))
        # regulators
        self.player_speed_regulator = reg.Regulator(int(2.1 * self.display.get_width() / 3), int(3 * self.display.get_height() / 10), 'Player Speed')
        self.enemy_multiplier_regulator = reg.Regulator(int(2.1 * self.display.get_width() / 3), int(4 * self.display.get_height() / 10), 'Enemy Multiplier')
        self.player_attack_multiplier_regulator = reg.Regulator(int(2.1 * self.display.get_width() / 3), int(5 * self.display.get_height() / 10), 'Player Attack Multiplier')
        self.player_projectile_speed_regulator = reg.Regulator(int(2.1 * self.display.get_width() / 3), int(6 * self.display.get_height() / 10), 'Player Projectile Speed')
        self.enemy_projectile_speed_regulator = reg.Regulator(int(2.1 * self.display.get_width() / 3), int(7 * self.display.get_height() / 10), 'Enemy Projectile Speed')
        # music
        self.music_manager = reg.Regulator_music(int(2.5 * self.display.get_width() / 3), int(9 * self.display.get_height() / 10), 'Music')
        # ambiante
        self.bush_cords = self.bush_chords
        
    # blit verwendet die von pygame bereitgestellte blit funktion um, eine Oberflaeche wie ein Bild an einer bestimmten
    # Position auf dem Displaysurface darzustellen
    def blit(self, surface, pos_x, pos_y):
        self.display.blit(surface, (pos_x,pos_y))
    
    # draw_rect verwendet die von pygame bereitgestellte draw.rect Funktion
    # um ein Rect Objekt auf einen Surface zu zeichnen
    def draw_rect(self, rect):
        pygame.draw.rect(self.display, 'black', rect)
    
    # render_text zeichent Text auf den Bildschirm
    # text: Inhalt, size: Schriftgroesse, x,y:position, color: Schriftfarbe (r,g,b)
    def render_text(self, text, size, x, y, color):
        font_obj = pygame.font.SysFont(None, size)
        surf_obj = font_obj.render(text, True, color)
        self.blit(surf_obj, x, y)

    def draw_regulator(self, regulator, variable):
        self.render_text(f'{regulator.text}: {int(variable)}', int(self.display.get_height() / 30), regulator.text_x, regulator.text_y, (255,255,255))
        pygame.draw.rect(self.display, (30,30,30), regulator.minus_rect)
        pygame.draw.rect(self.display, (30,30,30), regulator.plus_rect)
        self.blit(regulator.plus_img, regulator.plus_x, regulator.plus_y)
        self.blit(regulator.minus_img, regulator.minus_x, regulator.minus_y)
    
    def draw_music_manager(self, regulator, variable, music_paused):
        self.render_text(f'{regulator.text} ({int(variable)})', int(self.display.get_height() / 30), regulator.text_x, regulator.text_y, (255,255,255))
        pygame.draw.rect(self.display, (30,30,30), regulator.minus_rect)
        pygame.draw.rect(self.display, (30,30,30), regulator.plus_rect)
        pygame.draw.rect(self.display, (30,30,30), regulator.skip_rect)
        self.blit(regulator.plus_img, regulator.plus_x, regulator.plus_y)
        self.blit(regulator.minus_img, regulator.minus_x, regulator.minus_y)
        self.blit(regulator.skip_img, regulator.skip_x, regulator.skip_y)
        if music_paused == False:
            pygame.draw.rect(self.display, (30,30,30), regulator.pause_rect)
            self.blit(regulator.pause_img, regulator.pause_x, regulator.pause_y)
        if music_paused == True:
            pygame.draw.rect(self.display, (30,30,30), regulator.unpause_rect)
            self.blit(regulator.unpause_img, regulator.pause_x, regulator.pause_y)
    # update ist die die Routine in der alle statischen Bildelemente jedes Frame neu dargestellt werden 
    
    def update(self):
        self.display.fill((0,0,0))
        pygame.draw.rect(self.display, (255,255,255), self.game_screen)
        pygame.draw.rect(self.display, (30,30,30), self.stat_screen)
        
        
