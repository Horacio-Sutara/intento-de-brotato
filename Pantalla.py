import pygame
import Constantes as const
import Objeto 


jugador=Objeto.Objeto(50,50)






pygame.init()

ancho=const.ANCHO_VENTANA
alto=const.ALTO_VENTANA

ventana=pygame.display.set_mode((ancho,alto))
pygame.display.set_caption("")

run =True

while run:

    jugador.dibujar(ventana)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    pygame.display.update()


pygame.quit()
