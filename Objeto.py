import pygame

class Objeto():
    def __init__(self, x=20, y=30, imagenes=[], intervalo_cambio=0):

        self.visible=True

        self.imagenes = imagenes
        self.indice_imagen = 0  # Índice para controlar qué imagen mostrar
        self.rect_imagen = self.imagenes[self.indice_imagen].get_rect()
        self.rect_imagen.topleft = (x, y)
        self.indice = 0
        self.intervalo_cambio = intervalo_cambio  # Intervalo de tiempo en milisegundos para cambiar la imagen
        self.acumulador_tiempo=0
        self.posicion_inicial_x=x
        self.posicion_inicial_y=y
        
        # Crear el rectángulo de colisión más pequeño
        self.rect_colision = pygame.Rect(x, y, self.rect_imagen.width, self.rect_imagen.height)

    def dibujar(self, interfaz):
        if self.visible:
            # Dibujar la imagen actual
            imagen_actual = self.imagenes[self.indice_imagen]
            interfaz.blit(imagen_actual, self.rect_imagen.topleft)

    def cambiar_imagen(self,disminuir=None,tiempo=17):

        self.acumulador_tiempo+=tiempo
        if self.acumulador_tiempo>= self.intervalo_cambio:
            self.indice += 1
            if disminuir is not None:
                self.indice-=2
            if self.indice >= len(self.imagenes):
                self.indice = 0
            if self.indice<0:
                self.indice=9
            self.indice_imagen = self.indice
            self.rect_imagen = self.imagenes[self.indice_imagen].get_rect()
            self.rect_imagen.topleft = self.rect_colision.topleft
            self.acumulador_tiempo -=self.intervalo_cambio
    def cambiar_imagen_indice(self,indice):
        self.indice=indice
        self.indice_imagen=indice
        self.rect_imagen = self.imagenes[self.indice_imagen].get_rect()
        self.rect_imagen.topleft = self.rect_colision.topleft
        self.acumulador_tiempo-=self.acumulador_tiempo

    def verificar_colision(self, otro_rect):
        if self.visible:
            # Verificar colisión con el rectángulo de colisión más pequeño
            return self.rect_colision.colliderect(otro_rect)
        else: return False

    def mostrar_objeto(self):
        self.visible=True
    def desaparecer(self):
        self.visible=False
    
    def reposicionar(self,x=None,y=None):
        if x is None:
            x=self.posicion_inicial_x
        if y is None:
            y=self.posicion_inicial_y
        self.rect_colision.x=x
        self.rect_colision.y=y
        self.rect_imagen.x=x
        self.rect_imagen.y=y
class Movimiento(Objeto):

    def __init__(self, x=20, y=30, imagenes=[], intervalo_cambio=500):
        super().__init__(x, y, imagenes, intervalo_cambio)
        self.x=x
        self.y=y
        self.velocidad=1
    def mover_izquierda(self,mover=None):
        
        if mover is not None:
            self.velocidad=mover

        if self.rect_imagen.x>=22:
            self.rect_imagen.x-=self.velocidad
            self.rect_colision.x-=self.velocidad

    def mover_derecha(self,mover=None):
        if mover is not None:
            self.velocidad=mover
        if self.rect_imagen.x<=925:
            self.rect_imagen.x+=self.velocidad
            self.rect_colision.x+=self.velocidad

    def mover_arriba(self,mover=None):
        if mover is not None:
            self.velocidad=mover
        if self.rect_imagen.y>=115:
            self.rect_imagen.y-=self.velocidad
            self.rect_colision.y-=self.velocidad
            

    def mover_abajo(self,mover=None):
        if mover is not None:
            self.velocidad=mover
        if self.rect_imagen.y<=700:
            self.rect_imagen.y +=self.velocidad
            self.rect_colision.y +=self.velocidad

    def resetear_velocidad(self):
        self.velocidad=1


class vida(Objeto):
    def __init__(self, x=20, y=30, imagenes=[], intervalo_cambio=0,hp=8):
        super().__init__(x, y, imagenes, intervalo_cambio)
        self.hp=hp
        self.hp_max=hp
        self.hp_inicial=hp
    def regular_vida(self,daño=None,curar=None):
        
        if daño is not None:
            self.hp-=daño
        if curar is not None:
            self.hp+=curar
        
        if self.hp>self.hp_max and curar is not None:self.hp=self.hp_max
        if self.hp<0:self.hp=0

        porcentaje=(self.hp*100)//self.hp_max
        indice=((len(self.imagenes)-1)*porcentaje)//100
        indice=len(self.imagenes)-indice-1
        self.cambiar_imagen_indice(indice=indice)
    def resetear(self):
        self.hp_max=self.hp_inicial
        self.hp=self.hp_inicial
        self.regular_vida()

    def aumentar_hp(self,cantidad=1):
        self.hp_max+=cantidad
        self.regular_vida()
