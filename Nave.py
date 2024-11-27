import pygame

class Nave:
    '''Clase que gestiona la nave del jugador'''

    def __init__(self, juego):
        """Inicializa la nave y su posición inicial"""

        self.screen = juego.screen
        self.ajustes = juego.ajustes
        self.screen_rect = juego.screen.get_rect()

        #cargar la imagen de la nave y obtener sus dimensiones
        self.image = pygame.image.load('naveimagen.bmp')
        self.rect = self.image.get_rect()
        

        self.rect.midbottom = self.screen_rect.midbottom

        #guardar un valor decimal para la posición horizontal de la nave
        self.x = float(self.rect.x)
        #gestionar el movimiento de la nave

        self.movimiento_derecha = False
        self.movimiento_izquierda = False

    def actualizar_nave(self):
        '''Actualiza la posición de la nave basada en el movimiento'''
        if self.movimiento_derecha and self.rect.right < self.screen_rect.right:
            self.x += self.ajustes.velocidad_nave

        elif self.movimiento_izquierda and self.rect.left > 0:
            self.x -= self.ajustes.velocidad_nave
        self.rect.x = self.x

    def blitme(self):
        '''Inicia la imagen de la nave en pantalla'''
        self.screen.blit(self.image, self.rect)