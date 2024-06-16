import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

print("\nQuestão 2\n", "Desenvolver uma aplicação gráfica interativa onde o usuário poderá desenhar pontos na tela ao clicar com o mouse. Esta atividade deverá ser realizada utilizando a integração entre Pygame e OpenGL, bem como os conceitos básicos de manipulação de eventos e renderização gráfica.")

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("QUESTÃO 2")

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 640, 0, 480)


def plot_point():
    glBegin(GL_POINTS)
    glVertex2f(0, 0)
    glEnd()


done = False

init_ortho()
glPointSize(5)

while not done:
    mouse_postion = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type ==MOUSEBUTTONDOWN:
             mouse_postion = pygame.mouse.get_pos()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    if mouse_postion is not None:
        plot_point(mouse_postion)
    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()
