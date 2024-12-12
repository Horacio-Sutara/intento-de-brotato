import pygame


class Objeto():
    def __init__(self,x=20,y=30,):
        self.forma= pygame.Rect(0,0,50,80)
        self.forma.center=(x,y)

    def dibujar (self, interfaz):
        pygame.draw.rect(interfaz,(255,255,0),self.forma)
