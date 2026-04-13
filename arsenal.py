"""
Program Name: arsenal.py
My name: Ishan Agarwal
Purpose: This file contains the class that is responsible for managing the ship's bullets (including firing and updating them).
Starter Code: No
Date: 04/12/2026
"""


import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

import bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class ShipArsenal:
    """
    This class is responsible for managing the bullets, including firing and updating them
    """

    def __init__(self, game: 'AlienInvasion') -> None:
        """
        This initializes the arsenal class
        """

        self.game = game
        self.settings = game.settings
        
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self) -> None:
        """
        Update the position of the bullets in arsenal, along with the inventory of bullets on screen
        """
        
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self) -> None:
        """
        This removes the bullets that have gone off screen (called in the previous method)
        """

        for bullet in self.arsenal.copy():
            if bullet.rect.left >= self.game.screen.get_rect().right:
                self.arsenal.remove(bullet)

    def draw(self) -> None:
        """
        Draw the bullets
        """

        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        """
        Fire a bullet if there are less than the limit on screen
        """

        if len(self.arsenal) < self.settings.bullets_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False