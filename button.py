import pygame.font

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import ShipArsenal

class Button:
    """ 
    This class represents the button that will be used to start the game
    """

    def __init__(self, game: 'AlienInvasion', msg) -> None:
        """
        This initializes the button class using information from settings
        """

        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.setting = game.settings
        self.font = pygame.font.Font(self.setting.font_file, 
                                     self.setting.button_font_size)
        self.rect = pygame.Rect(0, 0, self.setting.button_w, self.setting.button_h)
        self.rect.center = self.boundaries.center
        self._prep_msg(msg)

    def _prep_msg(self, msg) -> None:
        """
        This method turns the msg into a rendered image and centers it on the button
        """

        self.msg_image = self.font.render(msg, True, self.setting.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self) -> None:
        """
        This method draws the button on the screen
        """

        self.screen.fill(self.setting.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos) -> bool:
        """
        This method checks if the button has been clicked
        """
        
        return self.rect.collidepoint(mouse_pos)