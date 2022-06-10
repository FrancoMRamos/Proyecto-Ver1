import pygame       #Importamos la librería Pygame
from pygame.locals import *     #Con esto estamos todos los módulos locales de Pygame

pygame.init()

clock = pygame.time.Clock()     #Para que se repita la imagen cada cierto tiempo
fps = 60        

#Tamaño del entorno
screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')


#Definimos las variables del juego.
ground_scroll = 0
scroll_speed = 4

#Cargamos las imagenes.
bg = pygame.image.load('img/bg.png')
ground_img = pygame.image.load('img/ground.png')

# Realizamos una clase para el pájaro, en la que están los 3 sprites del mismo que nos ayudarán para su animación.
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(f'img/bird{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):

        # Manejamos la animación, este será 
        self.counter += 1
        flap_cooldown = 5

        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]


bird_group = pygame.sprite.Group()

flappy = Bird(100, int(screen_height / 2))

bird_group.add(flappy)


run = True
while run:

    clock.tick(fps)     #Este método nos ayudará a manejar la tasa de fotogramas del programa

    # Agregamos el fondo
    screen.blit(bg, (0,0))

    bird_group.draw(screen)
    bird_group.update()

    # Agregando el suelo
    screen.blit(ground_img, (ground_scroll, 768))
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0

    # Para cerrar el programa, se deberá presionar la X de la ventana de Windows
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()