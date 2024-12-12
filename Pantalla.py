import pygame
import random
import Constantes as const
import Objeto 



class Ventana():
    def __init__(self,ancho,alto,fondo):
        pygame.init()
        self.ventana=pygame.display.set_mode((ancho,alto))
        pygame.display.set_caption("prueba")
        self.reloj =pygame.time.Clock()
        self.tiempo_inicio = pygame.time.get_ticks()

        self.fondo=fondo
        #Objetos
        self.jugador=Objeto.Movimiento(900,50,const.IMAGEN_PJ,100)

        self.fruta=Objeto.Objeto(100,70,const.FRUTA)

        self.temporizador1=Objeto.Objeto(440,50,const.NUMEROS,10000)
        self.temporizador2=Objeto.Objeto(510,50,const.NUMEROS,1000)


    def __temporizador(self): 
        tiempo_actual = pygame.time.get_ticks() 
        segundos_transcurridos = (tiempo_actual - self.tiempo_inicio) // 1000 
        return segundos_transcurridos

    def __generar_manzana(self):
        self.fruta.reposicionar(random.randint(22, 925),random.randint(15, 600))
        self.fruta.mostrar_objeto()

    def ejecutar(self):
        run =True

        while run:
            #Mostrar en pantalla
            self.ventana.blit(self.fondo,(0,0))
            self.jugador.dibujar(self.ventana)
            self.fruta.dibujar(self.ventana)
            self.temporizador1.dibujar(self.ventana)
            self.temporizador2.dibujar(self.ventana)
            #Cambiar sprite
            self.jugador.cambiar_imagen()
            self.temporizador1.cambiar_imagen()
            self.temporizador2.cambiar_imagen()

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
            teclas = pygame.key.get_pressed() 
            if teclas[pygame.K_a] or teclas[pygame.K_LEFT]: 
                self.jugador.mover_izquierda() 
            if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]: 
                self.jugador.mover_derecha() 
            if teclas[pygame.K_w] or teclas[pygame.K_UP]: 
                self.jugador.mover_arriba() 
            if teclas[pygame.K_s] or teclas[pygame.K_DOWN]: 
                self.jugador.mover_abajo()

            if self.jugador.verificar_colision(self.fruta.rect_colision) and self.fruta.visible:
                self.fruta.desaparecer()
                print("¡Colisión detectada!")

            if not self.fruta.visible:
                aparecer_fruta=random.randint(0,1000)
                if aparecer_fruta==10:
                    self.__generar_manzana()


            

            pygame.display.flip()  # Actualizar pantalla
            


        pygame.quit()


ventana=Ventana(const.ANCHO_VENTANA,const.ALTO_VENTANA,const.BG)
ventana.ejecutar()