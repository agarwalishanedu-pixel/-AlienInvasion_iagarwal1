import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import ShipArsenal


class Ship:

    def __init__(self, game: 'AlienInvasion', arsenal: 'ShipArsenal') -> None:
        """
        This initializes the ship class using information/functions from the other classes
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image,
                                            (self.settings.ship_w, self.settings.ship_h))
        self.image = pygame.transform.rotate(self.image, -90)

        self.rect = self.image.get_rect()
        self.rect.midleft = self.boundaries.midleft
        self.moving_up = False
        self.moving_down = False
        self.y = float(self.rect.y)
        self.arsenal = arsenal

    def update(self) -> None:
        #updating the position of the ship based on the movement flags
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        temp_speed = self.settings.ship_speed
        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= temp_speed
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += temp_speed

        self.rect.y = self.y


    def draw(self) -> None:
        """
        This method does the drawing on screen, and will be called from the main game class
        """
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)
        

    def fire(self) -> bool:
        return self.arsenal.fire_bullet()