import sys
import pygame
from settings import Settings
from ship import Ship

# This is the game class that contains the various methods
class AlienInvasion:

    def __init__(self) -> None:
        """
        This is initializing the class and creating that initial display.
        """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, 
                                         (self.settings.screen_w, self.settings.screen_h))

        self.running: bool = True
        self.clock = pygame.time.Clock()

        self.ship = Ship(self)
    
    def run_game(self):
        """
        This will contain the game loop
        """
        while self.running:
            self._check_events()   
               
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _update_screen(self):
        # This is adding the images in order
        # Background 
        self.screen.blit(self.bg, (0, 0))

        #Ship
        self.ship.draw()
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            


if __name__ == '__main__':
    # Create an instance of the object
    ai = AlienInvasion()
    ai.run_game()