from typing import Any

import pygame as py
from pygame.sprite import Sprite

class Alien(Sprite):
    """una clase para representar un solo alien de la flota"""

    def __init__(self, juego):
        super().__init__()
        self.pantalla = juego.screen
        self.ajustes = juego.ajustes
        self.alien_vel = self.ajustes.alien_vel
        

        #carga la imagen del alien y la conigura su atributo rect.
        self.image = py.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        #inicia un nuevo alien cerca de la parte superior izquierda

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #guarda la posicion horizontal exacta del alien

        self.x = float(self.rect.x)



    def check_edges(self):
        """devuelve True si el alien esta en el borde de la pantalla"""
        screen_rect = self.pantalla.get_rect()

        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        

    def update(self):
        """mueve el alien a la derecha/izquierda"""

        self.x +=(self.ajustes.alien_vel * self.ajustes.direccion_horda)
        self.rect.x =self.x