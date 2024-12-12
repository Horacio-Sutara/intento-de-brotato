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
        self.jugador=Objeto.Objeto(50,50,const.IMAGEN_PJ,100)

    def ejecutar(self):
        run =True

        while run:
            self.ventana.blit(self.fondo,(0,0))
            self.jugador.dibujar(self.ventana)
            self.jugador.cambiar_imagen()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False

            pygame.display.flip()  # Actualizar pantalla


        pygame.quit()


ventana=Ventana(const.ANCHO_VENTANA,const.ALTO_VENTANA,const.BG)
ventana.ejecutar()