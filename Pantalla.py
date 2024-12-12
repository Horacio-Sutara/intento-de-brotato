import pygame
import Constantes as const
import Objeto 



class Ventana():
    def __init__(self,ancho,alto):
        pygame.init()
        self.ventana=pygame.display.set_mode((ancho,alto))
        pygame.display.set_caption("prueba")

        #Objetos
        self.jugador=Objeto.Objeto(50,50)

    def ejecutar(self):
        run =True

        while run:

            self.jugador.dibujar(self.ventana)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False

            pygame.display.update()


        pygame.quit()


ventana=Ventana(const.ANCHO_VENTANA,const.ALTO_VENTANA)
ventana.ejecutar()