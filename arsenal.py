import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

import bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class ShipArsenal:
    def __init__(self, game: 'AlienInvasion') -> None:
        self.game = game
        self.settings = game.settings
        
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self) -> None:
        # Update the position of the bullets in arsenal
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self) -> None:
        for bullet in self.arsenal.copy():
            if bullet.rect.left >= self.game.screen.get_rect().right:
                self.arsenal.remove(bullet)

    def draw(self) -> None:
        # Draw the bullets
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        #fire the bullet if there are less than limit on screen
        if len(self.arsenal) < self.settings.bullets_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False