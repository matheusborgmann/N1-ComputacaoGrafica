import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

print("\nQuestão 2\n", "Desenvolver uma aplicação gráfica interativa onde o usuário poderá desenhar pontos na tela ao clicar com o mouse. Esta atividade deverá ser realizada utilizando a integração entre Pygame e OpenGL, bem como os conceitos básicos de manipulação de eventos e renderização gráfica.")

# Incializa o Pygame
pygame.init()

# Dimensões da tela
width = 800
height = 600

#Configurações do display
screen = pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("QUESTÃO 2")

# Configurações do viewport
glViewport(0, 0, height, width)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(0, height, 0, width)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

# Função para desenhar os pontos
def plot_point():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_POINTS)
    for p in mouse_points:
        glVertex2fv(p)
    glEnd()
    pygame.display.flip()


done = False

glPointSize(50)
mouse_points = []

# Laço para o pygame continuar aberto
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            pos_x, pos_y = event.pos
            pos_y = height - pos_y
            mouse_points.append((pos_x, pos_y))

    plot_point()

pygame.quit()
