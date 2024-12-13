import pygame
import random
import Constantes as const
import Objeto 



class Ventana():
    def __init__(self,ancho,alto,fondo,personaje_imagen,hp_imagenes,Numeros_imagen, fruta_imagen,enemigo1_imagen):
        pygame.init()
        self.ventana=pygame.display.set_mode((ancho,alto))
        pygame.display.set_caption("prueba")
        self.fondo=fondo
        #Objetos
        self.jugador=Objeto.Movimiento(900,200,personaje_imagen,100)
        self.hp=Objeto.vida(x=30,y=-50,imagenes=hp_imagenes)

        self.frutas=[Objeto.Objeto(random.randint(22, 925),random.randint(115, 700),fruta_imagen) for i in range (10)]
        self.enemigos=[Objeto.Movimiento(random.randint(22, 925),random.randint(115, 700),enemigo1_imagen,150) for i in range (10)]
        self.enemigos[len(self.enemigos)-1].desaparecer()
        for i in range (len(self.frutas)-1):
            self.frutas[i].desaparecer()    
            self.enemigos[i].desaparecer()

        self.temporizador2=Objeto.Objeto(510,20,Numeros_imagen,1000) 
        self.temporizador1=Objeto.Objeto(440,20,Numeros_imagen,10000)
        
        self.temporizador1.cambiar_imagen_indice(indice=5)  
        self.temporizador2.cambiar_imagen_indice(indice=9)        


    def __generar_objeto(self,objeto):
        objeto.reposicionar(random.randint(22, 925),random.randint(115, 700))
        objeto.mostrar_objeto()

    def __presion_teclas(self,objeto):
        teclas = pygame.key.get_pressed() 
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]: 
            objeto.mover_izquierda(2) 
        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]: 
            objeto.mover_derecha(3) 
        if teclas[pygame.K_w] or teclas[pygame.K_UP]: 
            objeto.mover_arriba(4) 
        if teclas[pygame.K_s] or teclas[pygame.K_DOWN]: 
            objeto.mover_abajo(5)
    def atrapar(self, enemigos, personaje):
        for i in range(len(enemigos)):
            if enemigos[i].rect_colision.x>personaje.rect_colision.x:
                enemigos[i].mover_izquierda()
            if enemigos[i].rect_colision.x<personaje.rect_colision.x:
                enemigos[i].mover_derecha()
            if enemigos[i].rect_colision.y<personaje.rect_colision.y:
                enemigos[i].mover_abajo()
            if enemigos[i].rect_colision.y>personaje.rect_colision.y:
                enemigos[i].mover_arriba()
    def ejecutar(self):
        run =True

        while run:
            #Mostrar en pantialla
            self.ventana.blit(self.fondo,(0,0))
            self.jugador.dibujar(self.ventana)
            self.hp.dibujar(self.ventana)
            for i in range(len(self.frutas)):
                self.frutas[i].dibujar(self.ventana)
                self.enemigos[i].dibujar(self.ventana)
            self.temporizador2.dibujar(self.ventana)
            self.temporizador1.dibujar(self.ventana)
            
            #Cambiar sprite
            self.jugador.cambiar_imagen()
            for i in range(len(self.enemigos)):
                self.enemigos[i].cambiar_imagen()
            self.temporizador1.cambiar_imagen(True)
            self.temporizador2.cambiar_imagen(True)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
            self.__presion_teclas(self.jugador)
            self.atrapar(self.enemigos,self.jugador)
            for i in range(len(self.frutas)):
                if self.jugador.verificar_colision(self.frutas[i].rect_colision) and self.frutas[i].visible:
                    self.frutas[i].desaparecer()
                    self.hp.regular_vida(curar=1)
                    print("¡Colisión detectada!")
                if self.jugador.verificar_colision(self.enemigos[i].rect_colision) and self.enemigos[i].visible:
                    self.enemigos[i].desaparecer()
                    self.hp.regular_vida(daño=1)
                    print("¡Colisión detectada!")
                if not self.frutas[i].visible:
                    aparecer_fruta=random.randint(0,10000)
                    if aparecer_fruta==10:
                        self.__generar_objeto(self.frutas[i])
                if not self.enemigos[i].visible:
                    aparecer_enemigo=random.randint(0,1000)
                    if aparecer_enemigo==10:
                        self.__generar_objeto(self.enemigos[i])
            if self.hp.hp==0:
                run=0
                print("perdistes")
            

            pygame.display.flip()  # Actualizar pantalla
            


        pygame.quit()


ventana=Ventana(const.ANCHO_VENTANA,const.ALTO_VENTANA,const.BG,const.IMAGEN_PJ,const.HP,const.NUMEROS,const.FRUTA,const.ENEMIGO_1)
ventana.ejecutar()