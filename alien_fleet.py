"""
Program Name: alien_fleet.py
My name: Ishan Agarwal
Purpose: This specific file is where I use the alien class and create the main fleet and functions. 
Starter Code: No, this is an entirely new file.
Date: 04/26/2026
"""


import pygame
from typing import TYPE_CHECKING

from alien import Alien

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:
    """
    This is the class for managing the fleet of aliens 
    """

    def __init__(self, game: 'AlienInvasion'):
        """
        Initialize the fleet
        """
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed 

        self.create_fleet()

    def create_fleet(self):
        """
        This creates the fleet and uses the specific functions for location
        """

        #Create the fleet of aliens
        alien_h = self.settings.alien_h
        screen_h = self.settings.screen_h
        alien_w = self.settings.alien_w
        screen_w = self.settings.screen_w

        half_screen = self.settings.screen_w // 2
        fleet_w, fleet_h = self.calculate_fleet_size(alien_h, screen_w, alien_w, screen_h, half_screen)
        
        x_offset, y_offset = self.caclulate_offsets(alien_h, screen_h, alien_w, half_screen, fleet_w, fleet_h)

        self._create_rectangle_fleet(alien_h, alien_w, fleet_w, fleet_h, x_offset, y_offset)

    def _create_rectangle_fleet(self, alien_h, alien_w, fleet_w, fleet_h, x_offset, y_offset):
        """
        This uses the calculations to create a rectangular fleet of aliens on the right half of the screen.
        """
        
        for col in range(fleet_w):
            for row in range(fleet_h):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset
                if row % 2 == 0 or col % 2 == 0:
                    continue
                self._create_alien(current_x, current_y)

    def caclulate_offsets(self, alien_h, screen_h, alien_w, half_screen, fleet_w, fleet_h):
        """
        This calculates the margins and offsets that are needed to make the fleet on the right half
        """
        fleet_vertical_space = fleet_h * alien_h
        fleet_horizontal_space = fleet_w * alien_w

        x_offset = int(half_screen + (half_screen - fleet_horizontal_space) // 2)
        y_offset = int((screen_h - fleet_vertical_space) // 2)
        return x_offset, y_offset


    def calculate_fleet_size(self, alien_h, screen_w, alien_w, screen_h, half_screen):
        """
        This calculates the number of aliens that can fit in the two axis.
        """

        fleet_w = (half_screen // alien_w)
        fleet_h = (screen_h // alien_h)

        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2


        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2


        return fleet_w, fleet_h


    def _create_alien(self, current_x: int, current_y: int):
        """
        This creates an alien
        """

        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)

    def draw(self):
        """
        This draws the fleet of aliens on the screen
        """

        alien: Alien
        for alien in self.fleet:
            alien.draw_alien()

    def _check_fleet_edges(self):
        """
        This is used to check when the fleet hits the top or bottom of screen, then changes direction and moves fleet closer to the ship 
        """

        alien: Alien
        for alien in self.fleet:
            if alien.check_edges():
                self.fleet_direction *= -1
                self.drop_alien_fleet()
                break
            
    def drop_alien_fleet(self):
        """        
        This moves the fleet closer to the ship when it hits the edge
        """

        alien: Alien
        for alien in self.fleet:
            alien.x -= self.fleet_drop_speed
            
    def update_fleet(self):
        """
        This updates the position of the fleet
        """
        
        self._check_fleet_edges()
        self.fleet.update()

    def check_destroyed_status(self):
        """
        This checks if the whole fleet is destroyed, and if that is the case, it returns true to reset the level
        """

        return not self.fleet

    def check_fleet_left(self):
        """
        This checks if the fleet has reached the left edge of the screen, and if that is the case, it returns true to reset the level
        """

        alien: Alien
        for alien in self.fleet:
            if alien.rect.left <= 0:
                return True
        return False

    
    def check_collisions(self, bullets):
        """
        Checks when bullet hits alien, and removes both from screen.
        """

        collisions = pygame.sprite.groupcollide(self.fleet, bullets, True, True)
        return collisions