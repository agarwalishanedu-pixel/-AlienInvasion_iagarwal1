"""
Program Name: bullet.py
My name: Ishan Agarwal
Purpose: This file contains the class that represents the bullets fired, which also include it's orientation and movement.
Starter Code: No
Date: 04/12/2026
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """
    This class represents the bullets themselves (sprite), which also include their orientation and movement
    """
    
    def __init__(self, game: 'AlienInvasion') -> None:
        """
        This initializes the bullet class, which includes the image, orientation, and positioning
        """

        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image,
                                            (self.settings.bullet_w, self.settings.bullet_h))
        self.image = pygame.transform.rotate(self.image, -90)
        
        self.rect = self.image.get_rect()
        self.rect.midleft = game.ship.rect.midright
        self.x = float(self.rect.x)

    def update(self) -> None:
        """
        Update the position of the bullet
        """

        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self) -> None:
        """
        Draw the bullet on screen
        """
        
        self.screen.blit(self.image, self.rect)