import pygame, sys
from keyimages import KeyImages

class Keys:
    """
    Main class to manage application behaviour
    """

    def __init__(self):
        """
        Initialise program resources
        """
        pygame.init()
        self.screen = pygame.display.set_mode((600, 720))
        pygame.display.set_caption("Key Presses")
        self.bg_colour = (255, 255, 255)
        self.keyimage = KeyImages(self)

    def run_app(self):
        """
        Starts main app loop.
        """
        while True:
            self._check_events()
            self._update_screen()
           
    def _check_events(self):
         #Watch for keyboard and mouse movements.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.keyimage.up = True
        elif event.key == pygame.K_DOWN:
            self.keyimage.down = True
        elif event.key == pygame.K_LEFT:
            self.keyimage.left = True
        elif event.key == pygame.K_RIGHT:
            self.keyimage.right = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.keyimage.up = False
        elif event.key == pygame.K_DOWN:
            self.keyimage.down = False
        elif event.key == pygame.K_LEFT:
            self.keyimage.left = False
        elif event.key == pygame.K_RIGHT:
            self.keyimage.right = False


    def _update_screen(self):
        #Sets background colour.
        self.screen.fill(self.bg_colour)
        self.keyimage.updates()
        self.keyimage.blitme()
        #Draw most recent screen
        pygame.display.flip()



if __name__ == "__main__":
    #Make app instance and run app
    keys_app = Keys()
    keys_app.run_app()
