import sys
import pygame as py
from Ajustes import Ajustes
from Nave import Nave
from pygame.sprite import Group
from Bala import Bala
from Aliens import Alien
from time import sleep


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
        #crea una nave
        self.nave = Nave(self) 

        #crea un grupo en el que se almacenaran las balas
        self.balas = Group()

        #crea un grupo en el que se almacenaran los aliens
        self.aliens = Group()

        self._ejercito()
        print("ejercito creado")

    def ejecutar_juego(self):
        """Bucle principal del juego"""
        while True:
            self._eventos()
            self.nave.actualizar_nave()
            self._actualizar_balas()
            self._actualizar_aliens()
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

#   BALAS
    def _disparar_bala(self):
        """Método para disparar una bala"""
        if len(self.balas) < self.ajustes.balas_permitidas:
            nueva_bala = Bala(self)
            self.balas.add(nueva_bala)

    def _actualizar_balas(self):
        """Método para actualizar las balas en pantalla"""
        self.balas.update()
        for bala in self.balas.copy():
            if bala.rect.bottom <= 0:
                self.balas.remove(bala)

        self._comprobar_aciertos()

    def _comprobar_aciertos(self):
        """comprueba si alguna bala ha impactado en un alien"""
        colisiones = py.sprite.groupcollide(self.balas, self.aliens, True, True)

        if not self.aliens:
            self.balas.empty()
            self._ejercito()
            self.ajustes.vel_descenso += 5


    def _ejercito(self):
        """crea el ejercito"""
        #hace un alien
        alien = Alien(self)
        alien_ancho, alien_alto = alien.rect.size
        
        espacio_disponible_x =self.ajustes.ancho_pantalla - (2 * alien_ancho)
        n_alien_x = espacio_disponible_x //(2 * alien_ancho)

        #determina el nuero de filas de aliens que caben en la pantalla
        nave_altura=self.nave.rect.height
        espacio_disponible_y = (self.ajustes.altura_pantalla - (3 * alien_alto) - nave_altura)

        n_filas = espacio_disponible_y  // (2 * alien_alto)

        #Crea la flota completa de aliens
        for numero_fila in range (n_filas-2):
            for numero_alien in range(n_alien_x+1):
                self._crear_alien(numero_alien, numero_fila)


    def _crear_alien(self, numero_alien, numero_fila):
        """crea los aliens para la fila indicada"""
        alien = Alien(self)
        alien_ancho, alien_alto = alien.rect.size
        alien.x = alien_ancho + 2 * alien_ancho * numero_alien
        alien.rect.x = alien.x 
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * numero_fila
        self.aliens.add(alien)


    def _pres_tecla(self, evento):      
        if evento.key == py.K_LEFT or evento.key == py.K_a:
            self.nave.movimiento_izquierda = True
        elif evento.key == py.K_RIGHT or evento.key == py.K_d:
            self.nave.movimiento_derecha = True
        elif evento.key == py.K_SPACE:
            self._disparar_bala()
        elif evento.key == py.K_q:
            sys.exit()

    def _sol_tecla(self, evento):
        if evento.key == py.K_LEFT or evento.key == py.K_a:
            self.nave.movimiento_izquierda = False
        elif evento.key == py.K_RIGHT or evento.key == py.K_d:
            self.nave.movimiento_derecha = False

    def _actualizar_imagen(self):
        """Método para actualizar la imagen en pantalla"""
        self.screen.fill(self.color_fondo)
        self.nave.dibu_nave()  # Dibujar la nave en pantalla
        for bala in self.balas.sprites():
            bala.dibu_bala()
        self.aliens.draw(self.screen)
        py.display.flip()


    def _actualizar_aliens(self):
        """Método para actualizar los aliens en pantalla"""
        self._check_borde_horda()
        self.aliens.update()
        if py.sprite.spritecollideany(self.nave, self.aliens):
            print("Nave golpeada")
            self._abatida()

    def _abatida(self):
        """responde al impacto de un alien en la nave"""

        #disminuye las vidas
        self.stats.naves -=1

        #se deshace de los aliens y balas restantes.
        self.aliens.empty()
        self.bala.empty()

        #crea una flota nueva y centra la nave.
        self._ejercito()
        self.nave.center_ship()
        sleep(0.5)
        
    def _check_borde_horda(self):
        """responde si algun alien ha llegado al borde"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._cambia_sentido()
                break

    def _cambia_sentido(self):
        """baja toda la horda y cambia el sentido"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.ajustes.vel_descenso
        self.ajustes.direccion_horda *= -1


if __name__ == "__main__":
    juego = AtaqueAlien()
    juego.ejecutar_juego()