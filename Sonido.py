import pygame

class Sonido:
    def __init__(self, archivo, canal=None):
        # Inicializa el módulo de sonido si no está ya inicializado
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        # Carga el archivo de sonido
        self.sonido = pygame.mixer.Sound(archivo)
        # Si no se pasa un canal, se asigna el primero disponible
        self.canal = canal if canal else pygame.mixer.find_channel()  # Encuentra un canal disponible
    
    def reproducir(self):
        """Reproduce el sonido en su canal específico"""
        if self.canal and not self.canal.get_busy():  # Verifica si el canal está libre
            self.canal.play(self.sonido)
    
    def detener(self):
        """Detiene el sonido si está reproduciéndose"""
        if self.canal:
            self.canal.stop()
    
    def ajustar_volumen(self, volumen):
        """Ajusta el volumen del sonido entre 0.0 y 1.0"""
        self.sonido.set_volume(volumen)
