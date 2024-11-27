import sys
import pygame
from Ajustes import Ajustes
from Nave import Nave

'''
Por hacer:
- Dar movimiento a la nave
- crear la clase Alien
- Dar movimiento al alien
- crear una flota
- iniciar la flota
'''

class AtaqueAlien:
    """Clase general para la gestión de los recursos y comportamiento del juego"""
    def __init__(self):
        pygame.init()
        self.ajustes = Ajustes()

        self.screen = pygame.display.set_mode(
            (self.ajustes.ancho_pantalla, self.ajustes.altura_pantalla))
        
        pygame.display.set_caption("Ataque Alien")
        self.color_fondo = (self.ajustes.color_fondo)
        self.nave = Nave(self)
        
    def ejecutar_juego(self):
        """Bucle principal del juego"""
        while True:
            self._eventos()
            self.nave.actualizar_nave()
            self._actualizar_imagen()

    def _eventos(self):
        """Método privado para la gestión de eventos como los imputs de teclado y raton"""
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    self.nave.movimiento_derecha = True
                if evento.key == pygame.K_LEFT:
                    self.nave.movimiento_izquierda = True
            
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_RIGHT:
                    self.nave.movimiento_derecha = False
                if evento.key == pygame.K_LEFT:
                    self.nave.movimiento_izquierda = False


    def _actualizar_imagen(self):
        """Método para actualizar la imagen en pantalla"""
        self.screen.fill(self.color_fondo) #Crea la imagen de la pantalla
        self.nave.blitme() #Dibujar la nave en pantalla
        pygame.display.flip()











if __name__ == "__main__":
    juego = AtaqueAlien()
    juego.ejecutar_juego()