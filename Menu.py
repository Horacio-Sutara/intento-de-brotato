import pygame
import Sonido
import sys
from Boton import Boton



class Menu():
    def __init__(self,ventana,fondo,x_boton_1,y_boton_1,imagen_boton1,x_boton_2,y_boton_2,imagen_boton2,boton_sonido):
        self.ventana=ventana
        self.inicio=False
        self.accion_boton_1=False
        self.accion_boton_2=False
        self.fondo=fondo

        self.boton_1=Boton(x_boton_1, y_boton_1, imagen_boton1)
        #cerrar
        self.boton_2=Boton(x_boton_2, y_boton_2, imagen_boton2)

        self.boton_sonido=Sonido.Sonido(boton_sonido)
        self.boton_sonido.ajustar_volumen(0.2)
    def mostrar(self):
        self.inicio=True
        while self.inicio:
            self.ventana.blit(self.fondo,(0,0))
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if self.boton_1.es_click(evento):
                    self.boton_sonido.reproducir()
                    self.inicio=False
                    self.accion_boton_1=True
                if self.boton_2.es_click(evento):
                    self.boton_sonido.reproducir()
                    self.inicio=False
                    self.accion_boton_1=False
                    self.accion_boton_2=True
            self.boton_1.dibujar(self.ventana)
            self.boton_2.dibujar(self.ventana)
            pygame.display.update()