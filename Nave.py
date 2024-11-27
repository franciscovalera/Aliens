import pygame

class Nave:
    '''Clase que gestiona la nave del jugador'''

    def __init__(self, juego):
        """Inicializa la nave y su posición inicial"""

        self.screen = juego.screen
        self.screen_rect = juego.screen.get_rect()

        #cargar la imagen de la nave y obtener sus dimensiones
        self.image = pygame.image.load('naveimagen.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        '''Inicia la imagen de la nave en pantalla'''
        self.screen.blit(self.image, self.rect)