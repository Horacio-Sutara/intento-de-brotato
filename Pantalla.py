import pygame
import Constantes as const
import Objeto 



class Ventana():
    def __init__(self,ancho,alto,fondo):
        pygame.init()
        self.ventana=pygame.display.set_mode((ancho,alto))
        pygame.display.set_caption("prueba")

        self.fondo=fondo
        #Objetos
        self.jugador=Objeto.Movimiento(900,50,const.IMAGEN_PJ,100)

    def ejecutar(self):
        run =True

        while run:
            self.ventana.blit(self.fondo,(0,0))
            self.jugador.dibujar(self.ventana)
            self.jugador.cambiar_imagen()
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

            pygame.display.flip()  # Actualizar pantalla


        pygame.quit()


ventana=Ventana(const.ANCHO_VENTANA,const.ALTO_VENTANA,const.BG)
ventana.ejecutar()