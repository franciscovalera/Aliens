class Ajustes:
    """Clase para guardar la configuración del juego"""
    def __init__(self):
        # Configuración de la pantalla
        self.ancho_pantalla = 1200
        self.altura_pantalla = 800
        self.color_fondo = (0, 0, 0)
        # Velocidad que en un futuro se podrá personalizar
        self.velocidad_nave = 1.5
        # Configuración de la bala
        self.velocidad_bala = 1.0
        self.color_bala = (60, 60, 60)
        self.ancho_bala = 3
        self.altura_bala = 15
        self.balas_permitidas = 20