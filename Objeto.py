import pygame

class Objeto():
    def __init__(self, x=20, y=30, imagenes=[], intervalo_cambio=500):

        self.visible=True

        self.imagenes = imagenes
        self.indice_imagen = 0  # Índice para controlar qué imagen mostrar
        self.rect_imagen = self.imagenes[self.indice_imagen].get_rect()
        self.rect_imagen.topleft = (x, y)
        self.indice = 0
        self.intervalo_cambio = intervalo_cambio  # Intervalo de tiempo en milisegundos para cambiar la imagen
        self.tiempo_ultimo_cambio = pygame.time.get_ticks()
        # Crear el rectángulo de colisión más pequeño
        self.rect_colision = pygame.Rect(x, y, self.rect_imagen.width, self.rect_imagen.height)

    def dibujar(self, interfaz):
        if self.visible:
            # Dibujar la imagen actual
            imagen_actual = self.imagenes[self.indice_imagen]
            interfaz.blit(imagen_actual, self.rect_imagen.topleft)

    def cambiar_imagen(self):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.tiempo_ultimo_cambio >= self.intervalo_cambio:
            self.indice += 1
            if self.indice >= len(self.imagenes):
                self.indice = 0
            self.indice_imagen = self.indice
            self.rect_imagen = self.imagenes[self.indice_imagen].get_rect()
            self.rect_imagen.topleft = self.rect_colision.topleft
            self.tiempo_ultimo_cambio = tiempo_actual

    def verificar_colision(self, otro_rect):
        if self.visible:
            # Verificar colisión con el rectángulo de colisión más pequeño
            return self.rect_colision.colliderect(otro_rect)
        else: return False

    def mostrar_objeto(self):
        self.visible=True
    def desaparecer(self):
        self.visible=False
    
    def reposicionar(self,x,y):
        self.rect_colision.x=x
        self.rect_colision.y=y
        self.rect_imagen.x=x
        self.rect_imagen.y=y
class Movimiento(Objeto):

    def __init__(self, x=20, y=30, imagenes=[], intervalo_cambio=500):
        super().__init__(x, y, imagenes, intervalo_cambio)
        self.x=x
        self.y=y
    def mover_izquierda(self,mover=1):
        
        if self.rect_imagen.x>=22:
            self.rect_imagen.x-=mover
            self.rect_colision.x-=mover

    def mover_derecha(self,mover=1):
        if self.rect_imagen.x<=925:
            self.rect_imagen.x+=mover
            self.rect_colision.x+=mover

    def mover_arriba(self,mover=1):
        if self.rect_imagen.y>=15:
            self.rect_imagen.y-=mover
            self.rect_colision.y-=mover
            

    def mover_abajo(self,mover=1):
        if self.rect_imagen.y<=600:
            self.rect_imagen.y +=mover
            self.rect_colision.y +=mover
