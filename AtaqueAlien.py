import sys
import pygame as py
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
        py.init()
        self.ajustes = Ajustes()

        self.screen = py.display.set_mode((0,0), py.FULLSCREEN)
        self.ajustes.ancho_pantalla = self.screen.get_rect().width
        self.ajustes.altura_pantalla = self.screen.get_rect().height
        
        py.display.set_caption("Ataque Alien")
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

        for evento in py.event.get():
            if evento.type == py.QUIT:
                sys.exit()
            elif evento.type == py.KEYDOWN:
                self._pres_tecla(evento)

            elif evento.type == py.KEYUP:
                self._sol_tecla(evento)




    def _pres_tecla(self, evento):      
        if evento.key == py.K_LEFT:
            self.nave.movimiento_izquierda = True
        
        elif evento.key == py.K_RIGHT:
            self.nave.movimiento_derecha = True

        elif evento.key == py.K_q:
            sys.exit()

    def _sol_tecla(self, event):
        if event.key == py.K_LEFT:
            self.nave.movimiento_izquierda = False
        elif event.key == py.K_RIGHT:
            self.nave.movimiento_derecha = False
        


    def _actualizar_imagen(self):
        """Método para actualizar la imagen en pantalla"""
        self.screen.fill(self.color_fondo) #Crea la imagen de la pantalla
        self.nave.blitme() #Dibujar la nave en pantalla
        py.display.flip()











if __name__ == "__main__":
    juego = AtaqueAlien()
    juego.ejecutar_juego()