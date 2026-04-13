import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import ShipArsenal


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


        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7) 


        self.ship = Ship(self, ShipArsenal(self))
    
    def run_game(self):
        """
        This will contain the game loop
        """
        while self.running:
            self._check_events()   
            self.ship.update()
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
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keyup_events(self, event) -> None:
        # This checks if key is released and changes the movement flag to false
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    
    def _check_keydown_events(self, event) -> None:
        # This does the different events based on which key is down
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
    # Create an instance of the object
    ai = AlienInvasion()
    ai.run_game()
 