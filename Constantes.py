import pygame
#Ventana
ANCHO_VENTANA=1000
ALTO_VENTANA=800
BG=pygame.image.load('image/fondo02.png')


# sonido
puntaje_sonido="Sound//puntaje.wav"
muerte_sonido="Sound//muerte.wav"
boton_sonido="Sound//boton.wav"
GOLPE_ENEMIGO="Sound//golpe_enemigo.wav"
CURA="Sound//cura.wav"
BALA_SONIDO="Sound//bala.wav"
#Personaje
ALTO_PERSONAJE=80
ANCHO_PERSONAJE=50

IMAGEN_PJ= [
    pygame.image.load('image/personaje01.png'), 
    pygame.image.load('image/personaje02.png'),
     pygame.image.load('image/personaje01.png'), 
    pygame.image.load('image/personaje03.png')
]

ARMA=[pygame.image.load('image/arma.png')
]
BALA=[pygame.image.load('image/bala.png')]
HP=[
    pygame.image.load('image/vida01.png'), 
    pygame.image.load('image/vida02.png'),
     pygame.image.load('image/vida03.png'), 
    pygame.image.load('image/vida04.png'),
    pygame.image.load('image/vida05.png'), 
    pygame.image.load('image/vida06.png'),
     pygame.image.load('image/vida07.png'), 
    pygame.image.load('image/vida08.png'),
    pygame.image.load('image/vida09.png'), 
    pygame.image.load('image/vida10.png'),
     pygame.image.load('image/vida11.png'), 
    pygame.image.load('image/vida12.png')



]
BOTON_REINTENTAR=[
    pygame.image.load('image/Volver-a-jugar.png'), 
    pygame.image.load('image/Volver-a-jugar1.png')
]
BOTON_MENU=[
    pygame.image.load('image/Volver-al-menu.png'), 
    pygame.image.load('image/Volver-al-menu1.png')
]

FRUTA=[pygame.image.load('image/fruta01.png')]
NUMEROS=[
    pygame.image.load('image/numero0.png'), 
    pygame.image.load('image/numero1.png'),
     pygame.image.load('image/numero2.png'), 
    pygame.image.load('image/numero3.png'),

    pygame.image.load('image/numero4.png'), 
    pygame.image.load('image/numero5.png'),
     pygame.image.load('image/numero6.png'), 
    pygame.image.load('image/numero7.png'),

    pygame.image.load('image/numero8.png'), 
    pygame.image.load('image/numero9.png')
]
DINERO=[
    pygame.image.load('image/dinero.png'), 
]
ENEMIGO_1=[
    pygame.image.load('image/monstruo01.png'), 
    pygame.image.load('image/monstruo02.png'),
]


