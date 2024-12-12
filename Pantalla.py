import pygame
import Constantes as const
import Objeto 



class Ventana():
    def __init__(self,ancho,alto):
        pygame.init()
        self.ventana=pygame.display.set_mode((ancho,alto))
        pygame.display.set_caption("prueba")

        #Objetos
        self.jugador=Objeto.Objeto(50,50,const.IMAGEN_PJ,100)

    def ejecutar(self):
        run =True

        while run:
            
            self.ventana.fill((0, 0, 0))  # Limpiar pantalla
            self.jugador.dibujar(self.ventana)
            self.jugador.cambiar_imagen()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False

            pygame.display.flip()  # Actualizar pantalla


        pygame.quit()


ventana=Ventana(const.ANCHO_VENTANA,const.ALTO_VENTANA)
ventana.ejecutar()