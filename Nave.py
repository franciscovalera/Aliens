import pygame as py

class Nave:
    def __init__(self, juego):
        """Inicializa la nave y establece su posición inicial"""
        self.screen = juego.screen
        self.ajustes = juego.ajustes
        self.image = py.image.load('./naveimagen.bmp')  # Asegúrate de que la imagen existe
        self.rect = self.image.get_rect()
        self.screen_rect = juego.screen.get_rect()

        # Posicionar la nave en el centro inferior de la pantalla
        self.rect.midbottom = self.screen_rect.midbottom

        # Movimiento
        self.movimiento_derecha = False
        self.movimiento_izquierda = False

    def actualizar_nave(self):
        """Actualiza la posición de la nave según las banderas de movimiento"""
        if self.movimiento_derecha and self.rect.right < self.screen_rect.right:
            self.rect.x += self.ajustes.velocidad_nave
        if self.movimiento_izquierda and self.rect.left > 0:
            self.rect.x -= self.ajustes.velocidad_nave

    def dibu_nave(self):
        """Dibuja la nave en su posición actual"""
        self.screen.blit(self.image, self.rect)