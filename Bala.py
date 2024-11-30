import pygame as py
from pygame.sprite import Sprite

class Bala(Sprite):
    """Clase para gestionar las balas disparadas por la nave."""
    def __init__(self, juego):
        super().__init__()
        self.screen = juego.screen
        self.color = (255, 0, 0)  
        self.velocidad = juego.ajustes.velocidad_bala  # Velocidad de la bala
        # Crear un rectángulo de bala en (0, 0) y luego establecer la posición correcta
        self.rect = py.Rect(0, 0, juego.ajustes.ancho_bala, juego.ajustes.altura_bala)
        self.rect.midtop = juego.nave.rect.midtop
        # Almacenar la posición de la bala como un valor decimal
        self.y = float(self.rect.y)

    def update(self):
        """Mueve la bala hacia arriba."""
        self.y -= self.velocidad  # Actualiza la posición en el eje Y
        self.rect.y = self.y  # Actualiza la posición del rectángulo

    def dibu_bala(self):
        """Dibuja la bala en la pantalla."""
        py.draw.rect(self.screen, self.color, self.rect)