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
        indice=None
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
        if indice is not None:
            self.apuntar(objetivos[indice].rect_imagen.x,objetivos[indice].rect_imagen.y)
        else:
            self.apuntar(self.rect_imagen.x-10,self.rect_imagen.y)

class Bala(Movimiento):

    def __init__(self, x=20, y=30, imagenes=..., intervalo_cambio=500):
        super().__init__(x, y, imagenes, intervalo_cambio)
        self.velocidad=0
        self.posicion_objetivo_x=0
        self.posicion_objetivo_y=0
        self.izquierda_x=False
        self.arriba_y=False
        self.angulo=0
    def disparar(self,x,y,objetivos,velocidad_inicial=7):
        self.reposicionar(x,y)
        self.mostrar_objeto()
        self.velocidad=velocidad_inicial
        self.angulo=self.direccion(objetivos)
        

    def desaparecer(self):
        if self.velocidad<=0:
            self.visible=False
    def blanco(self,objetivos):
        for objetivo in objetivos:
            if self.verificar_colision(objetivo.rect_colision) and objetivo.visible:
                self.visible=False
                objetivo.visible=False

    def detectar_proximo(self,objetivos):
        distancia_menor=1800
        indice=None
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
        if indice is not None:
            return objetivos[indice].rect_imagen.x,objetivos[indice].rect_imagen.y
        else:
            return self.rect_imagen.x-10,self.rect_imagen.y
    def direccion(self,objetivos):
        x,y =self.detectar_proximo(objetivos)
        self.posicion_objetivo_x=x
        self.posicion_objetivo_y=y
        delta_x=x-self.rect_imagen.x
        delta_y= y-self.rect_imagen.y
        return math.degrees(math.atan2(delta_y, delta_x))

    def mover(self, friccion=0.1):
        if self.visible:
            radianes = math.radians(self.angulo)
            self.rect_imagen.x += self.velocidad * math.cos(radianes)
            self.rect_imagen.y += self.velocidad * math.sin(radianes)
            self.rect_colision.x+= self.velocidad * math.cos(radianes)
            self.rect_colision.y+= self.velocidad * math.sin(radianes)
            self.velocidad -= friccion

class Pistola(Arma):
    def __init__(self,Balas,couldown,recarga,sonido_disparo,sonido_recarga, x=20, y=30, imagenes=..., intervalo_cambio=0):
        super().__init__(x, y, imagenes, intervalo_cambio)
        
        self.sonido_bala=sonido_disparo
        self.sonido_recarga=sonido_recarga
        self.balas=Balas
        self.bala_actual=len(self.balas)
        self.couldown=couldown
        self.recarga=recarga

    def disparar(self,enemigos):
        if self.bala_actual<len(self.balas):
            if not self.balas[self.bala_actual].visible:
                self.balas[self.bala_actual].disparar(self.rect_imagen.x,self.rect_imagen.y,enemigos)
                self.sonido_bala.reproducir()
        else:
            self.sonido_recarga.reproducir()
            # crear funcion recarga para continuar
            self.bala_actual=0
            if not self.balas[self.bala_actual].visible:
                self.balas[self.bala_actual].disparar(self.rect_imagen.x,self.rect_imagen.y,enemigos)
                self.sonido_bala.reproducir()
        
        self.bala_actual+=1
