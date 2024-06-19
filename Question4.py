import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import win32api
import math

win32api.MessageBox(0, "R: limpar a tela\nC: Mudar a cor\n↑: aumentar o tamanho dos pontos\n↓:diminuir o tamano dos pontos\nQ: Desenhar um quadrado\nB: Desenhar uma bola:\nT: desenhar um triangulo", "Comandos")
print("\nQuestão 4\n",
      "Tendo como base as atividades anteriores você deverá: \n",
      "A. Desenhar linhas conectando os pontos na ordem em que foram clicados.\n",
      "B. Implementar diferentes formas geométricas (como triângulos ou quadrados) que podem ser desenhadas ao clicar com o mouse." )


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


def plot_point():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPointSize(dot_size)
    glBegin(GL_POINTS)
    for p in mouse_points:
        glColor3fv(p[2])
        glVertex2fv(p[0:2])
    glEnd()
    if len(mouse_points) >= 2:  # Verifica se há pelo menos 2 pontos
        glBegin(GL_LINES)
        for i in range(len(mouse_points) - 1):
            glColor3fv(mouse_points[i][2])  # Define a cor da linha com a cor do ponto
            glVertex2fv(mouse_points[i][0:2])  # Ponto inicial da linha
            glVertex2fv(mouse_points[i + 1][0:2])  # Ponto final da linha
        glEnd()

    pygame.display.flip()


# Função para desenhar triangulos
def plot_triangle():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    for p in triangle_point:
        # Define como base o ponto clicado
        base_point = p

        offset = 50  # Tamanho do triangulo
        angle1 = math.radians(225)  # ajuste de angulo para o formato do triangulo

        # Calculo do segundo ponto relativo ao ponto incial
        second_point_x = base_point[0] + offset * math.cos(angle1)
        second_point_y = base_point[1] + offset * math.sin(angle1)

        # Calculo do terceiro ponto
        angle2 = math.radians(315)  # Ajuste de angulo para o sentido do triangulo
        third_point_x = base_point[0] + offset * math.cos(angle2)
        third_point_y = base_point[1] + offset * math.sin(angle2)

        # Aqui uma lista de todos os três pontos é criada
        triangle_cord = [base_point, (second_point_x, second_point_y, current_color),
                           (third_point_x, third_point_y, current_color)]

        glPointSize(dot_size)
        glBegin(GL_TRIANGLES)  # o GL_TRIANGLES Faz o desenho dos triangulos
        for point in triangle_cord:
            glColor3fv(point[2])
            glVertex2fv(point[0:2])
        glEnd()

    pygame.display.flip()


def plot_circle():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPointSize(dot_size)

    for p in circle_points:
        # Centro do circulo
        center_point = p

        # Define o raio do circulo baseado no tamanho do ponto
        radius = dot_size * 5

        # Passa para deixar o circulo mais "liso"
        steps = 64

        # lista para colocar os pontos do circulo dentro
        circle_point = []

        # Calculo dos pontos do circulo usando incrementos de angulos
        for i in range(steps):
            angle = math.radians(i * 360 / steps)
            x = center_point[0] + radius * math.cos(angle)
            y = center_point[1] + radius * math.sin(angle)
            circle_point.append((x, y, current_color))

        glBegin(GL_LINE_LOOP)  # GL_LINE_LOOP para desenhar um circulo
        for point in circle_point:
            glColor3fv(point[2])
            glVertex2fv(point[0:2])
        glEnd()

    pygame.display.flip()


def plot_square():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPointSize(dot_size)

    for p in square_points:

        # Ponto central do quadrado
        center_point = p

        # Define a largura baseada no tamanho do ponto
        side_length = dot_size * 5

        # Calculate half side length for easier calculations Calculo da metade da largura
        half_side = side_length / 2

        # Calculo dos quatro cantos do quadrado
        corners = [
            (center_point[0] - half_side, center_point[1] + half_side, current_color),
            (center_point[0] + half_side, center_point[1] + half_side, current_color),
            (center_point[0] + half_side, center_point[1] - half_side, current_color),
            (center_point[0] - half_side, center_point[1] - half_side, current_color),
        ]

        glBegin(GL_QUADS)  # GL_QUADS para desenhar os quadrados
        for corner in corners:
            glColor3fv(corner[2])
            glVertex2fv(corner[0:2])
        glEnd()
    pygame.display.flip()


done = False
dot_size = 5

# Cores disponiveis (branco, vermelho, verde, azul)

colors = [(255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255)]
color_index = 0
current_color = colors[0]

# booleanas para ativar os métodos de desenhos
draw_triangle = False
draw_circle = False
draw_square = False

# Matrizes de pontos
mouse_points = []
triangle_point = []
circle_points = []
square_points = []


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            # Verifica qual booleana esta ativa para realizar o respectivo desenho
            if draw_triangle:
                pos_x, pos_y = event.pos
                pos_y = height - pos_y
                triangle_point.append((pos_x, pos_y, current_color))
            elif draw_circle:
                pos_x, pos_y = event.pos
                pos_y = height - pos_y
                circle_points.append((pos_x, pos_y, current_color))
            elif draw_square:
                pos_x, pos_y = event.pos
                pos_y = height - pos_y
                square_points.append((pos_x, pos_y, current_color))
            else:
                pos_x, pos_y = event.pos
                pos_y = height - pos_y
                mouse_points.append((pos_x, pos_y, current_color))
        elif event.type == KEYDOWN:
            # Limpa as matrizes assim limpando a tela
            if event.key == K_r:
                mouse_points = []
                triangle_point = []
                square_points = []
                circle_points = []
            # Alterna entre a lista de core
            elif event.key == K_c:
                color_index = (color_index + 1) % len(colors)
                current_color = colors[color_index]
            # Aumenta o tamamnho dos pontos
            elif event.key == K_UP:
                if dot_size == 1:
                    dot_size = 5
                else:
                    dot_size = dot_size + 5
            # Diminui o tamanho dos pontos
            elif event.key == K_DOWN:
                dot_size = max(1, dot_size - 5)
            # Após pressionar uma dessas teclas ele passara a desenhar apenas o desenho respectivo
            elif event.key == K_t:
                draw_triangle = not draw_triangle
                draw_circle = False
                draw_square = False
            elif event.key == K_b:
                draw_circle = not draw_circle
                draw_triangle = False
                draw_square = False
            elif event.key == K_q:
                draw_square = not draw_square
                draw_circle = False
                draw_triangle = False
# Chamada das funções
    plot_triangle()
    plot_circle()
    plot_square()
    plot_point()

pygame.quit()
