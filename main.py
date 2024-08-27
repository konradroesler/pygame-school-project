# Alle noetigen Imports wie Module, insbesondere Pygame 
from sys import exit
import pygame
import Engine as eng
import Screen as scr
import Spieler as pla

# Pygame wird initialisiert     
pygame.init()
running = True

# Engine wird instanziert   
game = eng.Engine()
clock = pygame.time.Clock()
# Haupt-While-Schleife  
while running:
    # Fuer pygame relevante for Schleife, in der alle events wie das Druecken einer Taste behandelt werden
    for event in pygame.event.get():
        # MUSIC
        if event.type == game.MUSIC_END:
            pygame.mixer.music.queue(game.playlist[0])
            game.playlist.append(game.playlist[0])
            game.playlist.pop(0)
        # QUIT, Spiel wird abgebrochen
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
        # RESIZE, Fenster und Inhalt werden angepasst
        if event.type == pygame.VIDEORESIZE:
            game.screen.set_display_size(event.w, event.h)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_j:
                game.spieler.focus_disable()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                game.spieler.focus_enable()
        # alle elemente im rechten bildschirm, um die spielparameter zu veraendern
        # es wird bei jedem element auf kollision mit dem mauszeiger geprueft, waehrend die maustaste gedrueckt wird
        if event.type == pygame.MOUSEBUTTONUP:
            # START GAME 
            if (game.screen.start_game_rect.collidepoint(pygame.mouse.get_pos())) and game.running == False:
                game.restart()
            # RESTART GAME
            if (game.screen.retry_game_rect.collidepoint(pygame.mouse.get_pos())) and game.running == False:
                game.restart()
            # REGUALTOR: player speed
            if (game.screen.player_speed_regulator.plus_rect.collidepoint(pygame.mouse.get_pos())) and game.running == False:
                game.spieler.mov_speed += 2
            if (game.screen.player_speed_regulator.minus_rect.collidepoint(pygame.mouse.get_pos())) and game.running == False and game.spieler.mov_speed > 2:
                game.spieler.mov_speed -= 2
            # REGUALTOR: enemy multiplier
            if (game.screen.enemy_multiplier_regulator.plus_rect.collidepoint(pygame.mouse.get_pos())) and game.running == False:
                game.enemy_multiplier += 1
            if (game.screen.enemy_multiplier_regulator.minus_rect.collidepoint(pygame.mouse.get_pos())) and game.running == False and game.enemy_multiplier > 1:
                game.enemy_multiplier -= 1
            # REGULATOR: player attack multiplier
            if (game.screen.player_attack_multiplier_regulator.plus_rect.collidepoint(pygame.mouse.get_pos())) and game.running == False and game.spieler.attack_ticker_multiplier < game.spieler.max_ticker - 1 :
                game.spieler.attack_ticker_multiplier += 1
            if (game.screen.player_attack_multiplier_regulator.minus_rect.collidepoint(pygame.mouse.get_pos())) and game.running == False and game.spieler.attack_ticker_multiplier > 1:
                game.spieler.attack_ticker_multiplier -= 1
            # EXIT GAME
            if (game.screen.exit_game_rect.collidepoint(pygame.mouse.get_pos())) and game.running == True:
                game.running = False
                for gegner in game.gegner:
                    game.gegner.remove(gegner)
            # REGULATOR: player projectile speed
            if (game.screen.player_projectile_speed_regulator.plus_rect.collidepoint(pygame.mouse.get_pos())) and game.running == False:
                game.spieler.projectile_speed += 1
            if (game.screen.player_projectile_speed_regulator.minus_rect.collidepoint(pygame.mouse.get_pos())) and game.running == False and game.spieler.projectile_speed > 1:
                game.spieler.projectile_speed -= 1
            # REGULATOR: enemy projectile speed
            if (game.screen.enemy_projectile_speed_regulator.plus_rect.collidepoint(pygame.mouse.get_pos())) and game.running == False:
                game.enemy_projectile_speed += 1
            if (game.screen.enemy_projectile_speed_regulator.minus_rect.collidepoint(pygame.mouse.get_pos())) and game.running == False and game.enemy_projectile_speed > 1:
                game.enemy_projectile_speed -= 1
            # MUSIC MANAGER
            if (game.screen.music_manager.plus_rect.collidepoint(pygame.mouse.get_pos())) and game.music_volume < 100:
                game.music_volume += 10
                pygame.mixer.music.set_volume(game.music_volume / 100)
            if (game.screen.music_manager.minus_rect.collidepoint(pygame.mouse.get_pos())) and game.music_volume > 0:
                game.music_volume -= 10
                pygame.mixer.music.set_volume(game.music_volume / 100)
            if (game.screen.music_manager.unpause_rect.collidepoint(pygame.mouse.get_pos())) and game.music_paused == True:
                pygame.mixer.music.unpause()
                game.music_paused = False
                game.just_clicked = True
            if (game.screen.music_manager.pause_rect.collidepoint(pygame.mouse.get_pos())) and game.music_paused == False and game.just_clicked == False:
                pygame.mixer.music.pause()
                game.music_paused = True
            if (game.screen.music_manager.skip_rect.collidepoint(pygame.mouse.get_pos())):
                pygame.mixer.music.unload()
                pygame.event.post(game.MUSIC_END_EVENT)
                pygame.mixer.music.load(game.playlist[0])
                pygame.mixer.music.play()
                game.music_paused = False

    # Spiel Logik 
    game.run()
    # clock.tick: Framerate
    clock.tick(60)
