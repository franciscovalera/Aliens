class Ajustes:
    """Clase para guardar la configuración del juego"""
    def __init__(self):
        # Configuración de la pantalla
        self.ancho_pantalla = 1200
        self.altura_pantalla = 800
        self.color_fondo = (230, 230, 230)

        # velocidad que en un futuro se podrá personalizar
        self.velocidad_nave = 1.5