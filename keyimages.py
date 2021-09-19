import pygame


class KeyImages:
    """
    A class to manage images of keys.
    """

    def __init__(self, app):
        """
        Initialise keys and their positions.
        """
        self.screen = app.screen
        self.screen_rect = app.screen.get_rect()
        self.image = pygame.image.load("/Users/yaw.o.k/Documents/Pystudy/test_projects/Keys app/images/k1.bmp")
        self.rect = self.image.get_rect()

        #Load image in the middle of the screen.
        self.rect.center = self.screen_rect.center
        
        #key press flags
        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def updates(self):
        """
        Updates key images in resposes to key presses.
        """
        if self.up:
            self.image = pygame.image.load("/Users/yaw.o.k/Documents/Pystudy/test_projects/Keys app/images/k2.bmp")
        elif self.down:
            self.image = pygame.image.load("/Users/yaw.o.k/Documents/Pystudy/test_projects/Keys app/images/k3.bmp")
        elif self.left:
            self.image = pygame.image.load("/Users/yaw.o.k/Documents/Pystudy/test_projects/Keys app/images/k4.bmp")
        elif self.right:
            self.image = pygame.image.load("/Users/yaw.o.k/Documents/Pystudy/test_projects/Keys app/images/k5.bmp")
        else:
            self.image = pygame.image.load("/Users/yaw.o.k/Documents/Pystudy/test_projects/Keys app/images/k1.bmp")


    def blitme(self):
        """
        Draw image on screen.
        """
        self.screen.blit(self.image, self.rect)