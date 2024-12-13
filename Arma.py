import pygame
from Objeto import Movimiento
import math

class Arma (Movimiento):

    def __init__(self, x=20, y=30, imagenes=..., intervalo_cambio=0):
        super().__init__(x, y, imagenes, intervalo_cambio)
        self.angulo = 0  # Ángulo inicial de rotación
        self.flip_horizontal = False  # Controlar el flip horizontal
        self.flip_vertical = False    # Controlar el flip vertical

    def dibujar(self, interfaz):
        # Rotar y reflejar la imagen
        imagen_transformada = pygame.transform.rotate(self.imagenes[self.indice_imagen], round(self.angulo))
        imagen_transformada = pygame.transform.flip(imagen_transformada, self.flip_horizontal, self.flip_vertical)
        rect_transformado = imagen_transformada.get_rect(center=self.rect_imagen.center)
        interfaz.blit(imagen_transformada, rect_transformado.topleft)
    
    def rotar_antihorario(self, movimiento):
        if not self.flip_horizontal:
            self.angulo += movimiento
            if 270>self.angulo>90:
                self.flip_horizontal=True
                self.angulo-=2*movimiento
            elif self.angulo>270:
                print("hola")
        else:
            self.angulo-=movimiento
            if 90<self.angulo<=270:
                self.flip_horizontal=False
                self.angulo+=movimiento
                
        self.angulo %= 360  # Asegurarse de que el ángulo esté entre 0 y 359 grados
        print(self.angulo)

    def rotar_horario(self,movimiento):
        if not self.flip_horizontal:
            self.angulo -= movimiento
            if 270>self.angulo>90:
                self.flip_horizontal=True
        else:
            self.angulo+=movimiento
            if 90<self.angulo<270:
                self.flip_horizontal=False
                self.angulo-=movimiento
                
        self.angulo %= 360  # Asegurarse de que el ángulo esté entre 0 y 359 grados
        print(self.angulo)

    def reflejar(self, horizontal=False, vertical=False):
        self.flip_horizontal = horizontal
        self.flip_vertical = vertical

    def apuntar(self,x,y):
        delta_x=x-self.rect_imagen.x
        delta_y=y-self.rect_imagen.y
        angulo_radianes = math.atan2(delta_y, delta_x)
        angulo_grados = math.degrees(angulo_radianes)
        self.angulo=angulo_grados
        if 90<=angulo_grados<=180 or -180<=angulo_grados<=-90:
            self.flip_horizontal=False
            self.angulo-=180
            self.angulo=int(self.angulo)
            self.angulo*=-1
        if -90<angulo_grados<=0:
            self.flip_horizontal=True
            self.angulo+=360
        if 0<angulo_grados<=90:
            self.flip_horizontal=True
      

    def detectar_proximo(self,objetivos):
        distancia_menor=1800
        indice=0
        for i in range(len(objetivos)):
            
            if objetivos[i].visible:
                distancia_y= objetivos[i].rect_imagen.y-self.rect_imagen.y
                if distancia_y<0:distancia_y*=-1
                distancia_x=objetivos[i].rect_imagen.x-self.rect_imagen.x
                if distancia_x<0: distancia_x*=-1
                distancia_total=distancia_x+distancia_y
                if distancia_total<distancia_menor:
                    distancia_menor=distancia_total
                    indice=i
        self.apuntar(objetivos[indice].rect_imagen.x,objetivos[indice].rect_imagen.y)


class Bala(Movimiento):

    def __init__(self, x=20, y=30, imagenes=..., intervalo_cambio=500):
        super().__init__(x, y, imagenes, intervalo_cambio)
        self.velocidad=0
        self.adelante_x=False
        self.adelante_y=False

    def disparar(self,x,y,objetivos,velocidad_inicial=7):
        self.reposicionar(x,y)
        self.mostrar_objeto()
        self.velocidad=velocidad_inicial
        self.direccion(objetivos)

    def desaparecer(self):
        if self.velocidad<=0:
            self.visible=False
    
    def detectar_proximo(self,objetivos):
        distancia_menor=1800
        indice=0
        for i in range(len(objetivos)):
            
            if objetivos[i].visible:
                distancia_y= objetivos[i].rect_imagen.y-self.rect_imagen.y
                if distancia_y<0:distancia_y*=-1
                distancia_x=objetivos[i].rect_imagen.x-self.rect_imagen.x
                if distancia_x<0: distancia_x*=-1
                distancia_total=distancia_x+distancia_y
                if distancia_total<distancia_menor:
                    distancia_menor=distancia_total
                    indice=i
        return objetivos[indice].rect_imagen.x,objetivos[indice].rect_imagen.y
    
    def direccion(self,objetivos):
        x,y =self.detectar_proximo(objetivos)

        if self.rect_imagen.x<x:
            self.adelante_x=True
        else:
            self.adelante_x=False
        if self.rect_imagen.y<y:
            self.adelante_y=True
        else:
            self.adelante_y=False

    def mover(self,friccion=0.1):
            if self.visible:
                if self.adelante_x:
                    self.mover_derecha()
                else:
                    self.mover_izquierda()
                if self.adelante_y:
                    self.mover_abajo()
                else:
                    self.mover_arriba()
                self.velocidad-=friccion
        


