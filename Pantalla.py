import pygame
import random
import Constantes as const
import Objeto 
import Menu
import Sonido
from Arma import Arma
from Arma import Bala
class Ventana():
    def __init__(self,ancho,alto,fondo,personaje_imagen,
                 hp_imagenes,Numeros_imagen, fruta_imagen,enemigo1_imagen,boton_reintentar,
                 boton_menu,sonido_boton,sonido_golpe,sonido_cura,arma_imagen,bala_imagen,sonido_bala,
                 dinero_imagen,
                 fondo_inicio_sonido,fondo_batalla_sonido):
        pygame.init()
        self.ventana=pygame.display.set_mode((ancho,alto))
        pygame.display.set_caption("prueba")
        self.fondo=fondo
        #Objetos
        self.jugador=Objeto.Movimiento(900,200,personaje_imagen,100)
        self.hp=Objeto.vida(x=30,y=-50,imagenes=hp_imagenes,hp=3)

        self.frutas=[Objeto.Objeto(random.randint(22, 925),random.randint(115, 700),fruta_imagen) for i in range (10)]
        self.enemigos=[Objeto.Movimiento(random.randint(22, 925),random.randint(115, 700),enemigo1_imagen,150) for i in range (10)]

        self.temporizador2=Objeto.Objeto(510,20,Numeros_imagen,1000) 
        self.temporizador1=Objeto.Objeto(440,20,Numeros_imagen,10000)

        self.puntaje_1=Objeto.Objeto(720,20,Numeros_imagen,1000)
        self.puntaje_2=Objeto.Objeto(790,20,Numeros_imagen,1000)        
        self.puntaje_3=Objeto.Objeto(860,20,Numeros_imagen,1000)

        self.dinero=Objeto.Objeto(610,10,dinero_imagen)

        self.arma=Arma(850,240,arma_imagen)
        self.bala=[Bala(0,0,bala_imagen) for i in range (10)]


        self.menu_perder=Menu.Menu(self.ventana,fondo,420,200,boton_reintentar,420,400,boton_menu,sonido_boton)

        self.golpe_enemigo=Sonido.Sonido(sonido_golpe,pygame.mixer.Channel(0))
        

        self.sonido_bala=Sonido.Sonido(sonido_bala,pygame.mixer.Channel(1))
        self.cura=Sonido.Sonido(sonido_cura,pygame.mixer.Channel(2))
        self.sonido_empezar=Sonido.Sonido(fondo_inicio_sonido,pygame.mixer.Channel(3))
        self.sonido_batalla=Sonido.Sonido(fondo_batalla_sonido,pygame.mixer.Channel(3))

        self.golpe_enemigo.ajustar_volumen(0.2)
        self.sonido_bala.ajustar_volumen(0.15)
        self.cura.ajustar_volumen(0.25)
        self.sonido_empezar.ajustar_volumen(0.12)
        self.sonido_batalla.ajustar_volumen(0.12)



    def __generar_objeto(self,objeto):
        objeto.reposicionar(random.randint(22, 925),random.randint(115, 700))
        objeto.mostrar_objeto()

    def __presion_teclas(self,objetos):
        teclas = pygame.key.get_pressed() 
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            for objeto in objetos:
                objeto.mover_izquierda(3) 

        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]: 
            for objeto in objetos:
                objeto.mover_derecha(3) 
        if teclas[pygame.K_w] or teclas[pygame.K_UP]: 
            for objeto in objetos:
                objeto.mover_arriba(3) 
        if teclas[pygame.K_s] or teclas[pygame.K_DOWN]: 
            for objeto in objetos:
                objeto.mover_abajo(3)

    def atrapar(self, enemigos, personaje, velocidad=None):
        for i in range(len(enemigos)):
            if enemigos[i].rect_colision.x>personaje.rect_colision.x and enemigos[i].visible:
                enemigos[i].mover_izquierda(velocidad)
            if enemigos[i].rect_colision.x<personaje.rect_colision.x and enemigos[i].visible:
                enemigos[i].mover_derecha(velocidad)
            if enemigos[i].rect_colision.y<personaje.rect_colision.y and enemigos[i].visible:
                enemigos[i].mover_abajo(velocidad)
            if enemigos[i].rect_colision.y>personaje.rect_colision.y and enemigos[i].visible:
                enemigos[i].mover_arriba(velocidad)
    def ejecutar(self):
        for i in range (len(self.frutas)):
            self.frutas[i].desaparecer()    
            self.enemigos[i].desaparecer()
            self.enemigos[i].resetear_velocidad()

            self.bala[i].desaparecer()

        run =True
        self.hp.resetear()
        self.temporizador1.cambiar_imagen_indice(indice=5)  
        self.temporizador2.cambiar_imagen_indice(indice=9)   
        
        self.puntaje_1.cambiar_imagen_indice(0)
        self.puntaje_2.cambiar_imagen_indice(0)
        self.puntaje_3.cambiar_imagen_indice(0)

        self.arma.reposicionar()
        self.jugador.reposicionar()
        
        clock = pygame.time.Clock()

        self.tiempo_ronda= pygame.time.get_ticks()
        self.sonido_empezar.reproducir()
        while run:
            self.sonido_batalla.reproducir()
            tiempo=clock.tick(60)
            enemigo_visible=self.enemigo_visible(self.enemigos)
            #Mostrar en pantialla
            self.ventana.blit(self.fondo,(0,0))
            self.jugador.dibujar(self.ventana)
            self.arma.dibujar(self.ventana)
            self.hp.dibujar(self.ventana)
            self.dinero.dibujar(self.ventana)

            self.arma.detectar_proximo(self.enemigos)
            if enemigo_visible:
                for i in range (len(self.bala)):
                    if not self.bala[i].visible:
                        self.bala[i].disparar(self.arma.rect_imagen.x,self.arma.rect_imagen.y,self.enemigos)
                        self.sonido_bala.reproducir()
                        i=len(self.bala)
                    else:
                        self.bala[i].blanco(self.enemigos)

            for i in self.bala:
                if i.visible:
                    i.blanco(self.enemigos)
                    i.desaparecer()
                    i.mover()
                    i.dibujar(self.ventana)

            


            for i in range(len(self.frutas)):
                self.frutas[i].dibujar(self.ventana)
                self.enemigos[i].dibujar(self.ventana)


            self.temporizador2.dibujar(self.ventana)
            self.temporizador1.dibujar(self.ventana)
            self.puntaje_1.dibujar(self.ventana)
            self.puntaje_2.dibujar(self.ventana)
            self.puntaje_3.dibujar(self.ventana)

            #Cambiar sprite
            self.jugador.cambiar_imagen(tiempo=tiempo)
            for i in range(len(self.enemigos)):
                self.enemigos[i].cambiar_imagen(tiempo=tiempo)
            self.temporizador1.cambiar_imagen(True,tiempo=tiempo)
            self.temporizador2.cambiar_imagen(True,tiempo=tiempo)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
            self.__presion_teclas([self.jugador,self.arma])

            if pygame.time.get_ticks() -self.tiempo_ronda>15000:
                self.tiempo_ronda=pygame.time.get_ticks()
                self.enemigos[0].velocidad+=0.1
            self.atrapar(self.enemigos,self.jugador,self.enemigos[0].velocidad)
            
            
            for i in range(len(self.frutas)):
                if self.jugador.verificar_colision(self.frutas[i].rect_colision) and self.frutas[i].visible:
                    self.frutas[i].desaparecer()
                    self.hp.regular_vida(curar=1)
                    self.cura.reproducir()
                    print("¡Colisión detectada!")
                if self.jugador.verificar_colision(self.enemigos[i].rect_colision) and self.enemigos[i].visible:
                    self.enemigos[i].desaparecer()
                    self.hp.regular_vida(daño=1)
                    self.golpe_enemigo.reproducir()
                    print("¡Colisión detectada!")
                if not self.frutas[i].visible:
                    aparecer_fruta=random.randint(0,10000)
                    if aparecer_fruta==10:
                        self.__generar_objeto(self.frutas[i])
                if not self.enemigos[i].visible:
                    aparecer_enemigo=random.randint(0,1000)
                    if aparecer_enemigo==10:
                        self.__generar_objeto(self.enemigos[i])
            if self.hp.hp<=0:
                run=0
        
            

            pygame.display.flip()  # Actualizar pantalla
        
        self.sonido_batalla.detener()


    def enemigo_visible(self,enemigos):
        for i in enemigos:
            if i.visible:
                return True
        return False

    
    def juego(self):
        jugar=True
        while jugar:
            self.ejecutar()
            self.menu_perder.mostrar()
            if self.menu_perder.accion_boton_1:
                print("volver a jugar")
            if self.menu_perder.accion_boton_2:
                print("ir a menu")
                jugar=False

        pygame.quit()

ventana=Ventana(const.ANCHO_VENTANA,const.ALTO_VENTANA,const.BG,const.IMAGEN_PJ,
                const.HP,const.NUMEROS,const.FRUTA,const.ENEMIGO_1,const.BOTON_REINTENTAR,
                const.BOTON_MENU,const.boton_sonido,const.GOLPE_ENEMIGO,
                const.CURA,const.ARMA,const.BALA,const.BALA_SONIDO,
                const.DINERO,const.FONDO_INICIO_SONIDO,const.FONDO_BATALLA_SONIDO)
ventana.juego()