import sys
import pygame as py
from Ajustes import Ajustes
from Nave import Nave
from pygame.sprite import Group
from Bala import Bala

'''
Por hacer:
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
        self.balas = Group()
        self.nave = Nave(self) 

    def ejecutar_juego(self):
        """Bucle principal del juego"""
        while True:
            self._eventos()
            self.nave.actualizar_nave()
            self._actualizar_balas()
            self._actualizar_imagen()

    def _eventos(self):
        """Método privado para la gestión de eventos como los inputs de teclado y ratón"""
        for evento in py.event.get():
            if evento.type == py.QUIT:
                sys.exit()
            elif evento.type == py.KEYDOWN:
                self._pres_tecla(evento)
            elif evento.type == py.KEYUP:
                self._sol_tecla(evento)

    def _disparar_bala(self):
        """Método para disparar una bala"""
        if len(self.balas) < self.ajustes.balas_permitidas:
            nueva_bala = Bala(self)
            self.balas.add(nueva_bala)

    def _pres_tecla(self, evento):      
        if evento.key == py.K_LEFT:
            self.nave.movimiento_izquierda = True
        elif evento.key == py.K_RIGHT:
            self.nave.movimiento_derecha = True
        elif evento.key == py.K_SPACE:
            self._disparar_bala()
        elif evento.key == py.K_q:
            sys.exit()

    def _sol_tecla(self, evento):
        if evento.key == py.K_LEFT:
            self.nave.movimiento_izquierda = False
        elif evento.key == py.K_RIGHT:
            self.nave.movimiento_derecha = False

    def _actualizar_imagen(self):
        """Método para actualizar la imagen en pantalla"""
        self.screen.fill(self.color_fondo)
        self.nave.dibu_nave()  # Dibujar la nave en pantalla
        for bala in self.balas.sprites():
            bala.dibu_bala()
        py.display.flip()

    def _actualizar_balas(self):
        """Método para actualizar las balas en pantalla"""
        self.balas.update()
        for bala in self.balas.copy():
            if bala.rect.bottom <= 0:
                self.balas.remove(bala)

if __name__ == "__main__":
    juego = AtaqueAlien()
    juego.ejecutar_juego()