"""
Program Name: alien_invasion.py
My name: Ishan Agarwal
Purpose: This specific file is where the main game loop is, and where the different classes come together. 
Starter Code: Yes, primarily in the form of assets.
Date: 04/19/2026
"""

import sys
import pygame
from game_stats import GameStats
from settings import Settings
from ship import Ship
from arsenal import ShipArsenal
#from alien import Alien
from alien_fleet import AlienFleet
from time import sleep
from button import Button


# This is the game class that contains the various methods
class AlienInvasion:

    def __init__(self) -> None:
        """
        This is initializing the class and creating that initial display.
        """
        
        pygame.init()
        self.settings = Settings()
        self.settings.initialize_dynamic_settings()

        self.game_stats = GameStats(self.settings.starting_ship_count)

        self.screen = pygame.display.set_mode((self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, 
                                         (self.settings.screen_w, self.settings.screen_h))

        self.running: bool = True
        self.clock = pygame.time.Clock()


        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7) 

        self.impact = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact.set_volume(0.7) 

        self.ship = Ship(self, ShipArsenal(self))
        self.alien_fleet = AlienFleet(self)

        self.play_button = Button(self, 'Play')
        self.game_active = False
    

    def run_game(self):
        """
        This will contain the game loop
        """

        while self.running:
            self._check_events()   
            if self.game_active:    
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self):
        """
        This checks for the different scenarious of collisions and resets level accordingly
        """


        # Check for collisions for ship
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._check_game_status()
            # subtract one life if possible
    

        # Check collisions for aliens and bottom of screen
        if self.alien_fleet.check_fleet_left():
            self._check_game_status()

        # Check collisions of projecties and aliens
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact.play()
            self.impact.fadeout(250)

        # check if fleet is destroyed to reset level
        if self.alien_fleet.check_destroyed_status():
            self._reset_level()
            self.settings.increase_difficulty()
            # updatae game stats level
            # update HUD view
        
    def _check_game_status(self):
        """
        This checks the game status and resets the level if necessary
        """

        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False

        print(self.game_stats.ships_left)
    
    def _reset_level(self)-> None:
        """ 
        This will reset level by creating new fleet
        """
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()
        

    def restart_game(self):
        self.settings.initialize_dynamic_settings()
        # Reset game stats
        # Update HUD scores
        # reset level
        # recenter the ship
        self._reset_level()
        self.ship._center_ship()
        self.game_active = True
        pygame.mouse.set_visible(False)

    def _update_screen(self):
        """
        This is adding the images in order
        Background + Ship
        """
       
        self.screen.blit(self.bg, (0, 0))

        #Ship
        self.ship.draw()
        #Alien
        self.alien_fleet.draw()
        # draw HUD

        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)

        pygame.display.flip()

    def _check_events(self):
        """
        This is checking for the different events like key presses and releases, and quitting the game.
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and self.game_active == True:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def _check_button_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self.restart_game()
    
    def _check_keyup_events(self, event) -> None:
        """
        This checks if key is released and changes the movement flag to false
        """
        
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    
    def _check_keydown_events(self, event) -> None:
        """
        This handles the different events based on which key is pressed
        """

        if event.key == pygame.K_UP:
            self.ship.moving_up = True

        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)
        
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()
            

if __name__ == '__main__':
    """ 
    Create an instance of the object
    Runs the game
    """
    
    ai = AlienInvasion()
    ai.run_game()
 