"""
Program Name: alien.py
My name: Ishan Agarwal
Purpose: This specific file is where the alien sprite is created, and foundation for the fleet
Starter Code: NO
Date: 04/26/2026
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    """
    This class is the base for the alien sprite. It contains the methods for updating the position and drawing the alien on the screen
    """

    def __init__(self, fleet: 'AlienFleet', x: float, y: float) -> None:
        """
        this initializes the alien and sets the position of the alien
        """

        super().__init__()
        self.fleet = fleet

        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image,
                                            (self.settings.alien_w, self.settings.alien_h))
        self.image = pygame.transform.rotate(self.image, -90)
        
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self) -> None:
        """
        this updates the position of the alien based on the fleet's direction and speed
        """
        temp_speed = self.settings.fleet_speed 
        
        self.y += temp_speed * self.fleet.fleet_direction
        self.rect.y = self.y
        self.rect.x = self.x

    def check_edges(self) -> bool:
        """
        This checks if the alien has reached the top or bottom of the screen
        """

        return(self.rect.bottom >= self.boundaries.bottom or self.rect.top <= 0)


    def draw_alien(self) -> None:
        """
        This draws the alien on the screen
        """
        
        self.screen.blit(self.image, self.rect)