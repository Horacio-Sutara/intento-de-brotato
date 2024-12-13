import pygame

class Boton:
    def __init__(self, x, y, imagen):
        # Carga las imágenes para el estado normal y el estado "hover"
        self.pos_x_normal=x
        self.pos_y_normal=y
        self.imagen_normal = imagen[0]
        self.imagen_hover = imagen[1]
        self.imagen_actual = self.imagen_normal  # Imagen que se muestra actualmente
        self.rect = self.imagen_normal.get_rect()
        self.rect.topleft = (x, y)
        self.click = False  # Para verificar si se ha hecho clic

    def dibujar(self, ventana):
        # Cambia la imagen actual según la posición del mouse
        pos_mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos_mouse):
            self.imagen_actual = self.imagen_hover
            self.rect.topleft = (self.pos_x_normal-5, self.pos_y_normal)
        else:
            self.imagen_actual = self.imagen_normal
            self.rect.topleft = (self.pos_x_normal, self.pos_y_normal)

        # Dibuja la imagen actual en la ventana
        ventana.blit(self.imagen_actual, (self.rect.x, self.rect.y))

    def es_click(self, evento):
        # Comprueba si el botón ha sido clickeado
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(evento.pos):
                self.click = True  # Registra el clic

        if evento.type == pygame.MOUSEBUTTONUP:
            if self.click and self.rect.collidepoint(evento.pos):
                self.click = False
                return True  # Retorna True si se ha hecho clic correctamente
        return False

