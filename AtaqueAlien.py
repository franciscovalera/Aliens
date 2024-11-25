import sys
import pygame
from Ajustes import Ajustes

'''
Por hacer:
- Crear la nave
- Dar movimiento a la nave
- Iniciarla desde este archivo
'''

class AtaqueAlien:
    """Clase general para la gestión de los recursos y comportamiento del juego"""
    def __init__(self):
        pygame.init()
        self.ajustes = Ajustes()
        self.screen = pygame.display.set_mode((self.ajustes.ancho_pantalla, self.ajustes.altura_pantalla))
        pygame.display.set_caption("Ataque Alien")
        self.color_fondo = (self.ajustes.color_fondo)
        
    def ejecutar_juego(self):
        """Bucle principal del juego"""
        while True:
            # Escucha de eventos de teclado y ratón
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.color_fondo)
            # Actualización de la pantalla
            pygame.display.flip()

if __name__ == "__main__":
    juego = AtaqueAlien()
    juego.ejecutar_juego()