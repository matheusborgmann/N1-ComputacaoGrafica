import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


print("\nQuestão 5\n", "Nesta atividade, vocês irão criar uma aplicação gráfica que desenha uma forma geométrica básica como retângulos, triângulos e linhas. A forma geométrica terá que fazer sentido.")
print("inspirado em: https://cdn.dribbble.com/users/4538838/screenshots/14763174/media/ef7f391ae44801b0f74efa9837479f26.jpg?resize=400x300&vertical=center")

pygame.init()

width = 800
height = 600


screen = pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("QUESTÃO 5")


glViewport(0, 0, height, width)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(0, height, 0, width)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()


# Função para desenhar os pontos e conectalos
def plot_fox():
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
     glBegin(GL_LINES)
     for i in range(len(fox_head_points) - 1):
         glColor3fv(fox_head_points[i][2])  # Define a cor da linha com a cor do ponto
         glVertex2fv(fox_head_points[i][0:2])  # Ponto inicial da linha
         glVertex2fv(fox_head_points[i + 1][0:2])  # Ponto final da linha
     glEnd()

     pygame.display.flip()

# pontos da silhueta da cabeça
fox_head_points = [
     (334, 236, (0, 0, 255)),
     (354, 236, (0, 0, 255)),
     (384, 266, (0, 0, 255)),
     (464, 302, (0, 0, 255)),
     (450, 341, (0, 0, 255)),
     (455, 368, (0, 0, 255)),
     (440, 441, (0, 0, 255)),
     (384, 416, (0, 0, 255)),
     (314, 416, (0, 0, 255)),
     (258, 441, (0, 0, 255)),
     (253, 441, (0, 0, 255)),
     (238, 368, (0, 0, 255)),
     (248, 341, (0, 0, 255)),
     (234, 302, (0, 0, 255)),
     (314, 266, (0, 0, 255)),
     (334, 236, (0, 0, 255)),
]


def plot_fox_details():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_LINES)
    for i in range(len(fox_detail_points) - 1):
        glColor3fv(fox_detail_points[i][2])  # Define a cor da linha com a cor do ponto
        glVertex2fv(fox_detail_points[i][0:2])  # Ponto inicial da linha
        glVertex2fv(fox_detail_points[i + 1][0:2])  # Ponto final da linha
    glEnd()

    pygame.display.flip()


# pontos dos detalhes (olhos e nariz)
fox_detail_points = [

    (464, 302, (255, 255, 255)),
    (424, 302, (255, 255, 255)),
    (384, 306, (255, 255, 255)),
    (394, 316, (255, 255, 255)),
    (371, 312, (255, 255, 255)),
    (369, 302, (255, 255, 255)),
    (384, 306, (255, 255, 255)),
    (369, 302, (255, 255, 255)),
    (352, 256, (255, 255, 255)),
    (344, 246, (255, 255, 255)),
    (336, 256, (255, 255, 255)),
    (344, 260, (255, 255, 255)),
    (352, 256, (255, 255, 255)),
    (344, 260, (255, 255, 255)),
    (336, 256, (255, 255, 255)),
    (329, 302, (255, 255, 255)),
    (314, 306, (255, 255, 255)),
    (304, 316, (255, 255, 255)),
    (327, 312, (255, 255, 255)),
    (329, 302, (255, 255, 255)),
    (314, 306, (255, 255, 255)),
    (274, 302, (255, 255, 255)),
    (234, 302, (255, 255, 255)),

]


done = False


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
# Chamada das funções
    plot_fox()
    plot_fox_details()

pygame.quit()
