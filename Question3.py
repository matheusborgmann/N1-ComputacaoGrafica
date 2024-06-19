import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import win32api

win32api.MessageBox(0, 'R: limpar a tela\nC: Mudar a cor\n↑: aumentar o tamanho dos pontos\n↓:diminuir o tamano dos pontos', 'Comandos')
print("\nQuestão 3\n", "Tendo como base a atividade anterior, adicione recursos ao código criado na atividade 1 e 2:  \n",
      "A. Mude a cor dos pontos.\n",
      "B. Ajuste o tamanho dos pontos.\n",
      "C. Adicione um botão de reset para limpar todos os pontos.")


pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
pygame.display.set_caption("QUESTÃO 2")

# Configura o viewport
glViewport(0, 0, height, width)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(0, height, 0, width)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

# função para desenhar os pontos
def plot_point():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPointSize(dot_size)
    glBegin(GL_POINTS)
    for p in mouse_points:
        glColor3fv(p[2])
        glVertex2fv(p[0:2])
    glEnd()
    pygame.display.flip()


done = False
dot_size = 5

# Cores disponiveis (branco, vermelho, verde, azul)
colors = [(255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)]
color_index = 0
current_color = colors[0]


mouse_points = []

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            # salva a posição x e y do ponto do mouse
            pos_x, pos_y = event.pos
            pos_y = height - pos_y
            mouse_points.append((pos_x, pos_y, current_color))
        elif event.type == KEYDOWN:
            if event.key == K_r:
                # remove os pontos do array, assim removendo eles da tela
                mouse_points = []
            elif event.key == K_c:
                color_index = (color_index + 1) % len(colors)
                current_color = colors[color_index]
            elif event.key == K_UP:
                # licmita os pontos sempre de subirem em multiplos de 5
                if dot_size == 1:
                    dot_size = 5
                else:
                    dot_size = dot_size + 5
            elif event.key == K_DOWN:
                #  limita a 1 o tamanho do ponto
                dot_size = max(1, dot_size - 5)
# Chamada da função
    plot_point()

pygame.quit()
