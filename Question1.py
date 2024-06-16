import numpy as np

print("Questão 1\n", "Quantos pixels são colocados na tela por cada uma destas chamadas?")

# Calculo para saber a quantidade de pixels em g.drawLine(10, 20, 100, 50)
x1, y1 = 10, 20
x2, y2 = 100, 50
distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
# Aproximadamente 95 pixels
pixels_drawLine = int(np.round(distance))

# Calculo para saber a quantidade de pixels em g.drawRect(10, 10, 8, 5)
width = 8
height = 5
pixels_drawRect = (2 * width) + (2 * height) - 4

# Calculo para saber a quantidade de pixels em g.fillRect(10, 10, 8, 5)
pixels_fillRect = width * height

print(f"Pixels desenhados por g.drawLine(10, 20, 100, 50): {pixels_drawLine}")
print(f"Pixels desenhados por g.drawRect(10, 10, 8, 5): {pixels_drawRect}")
print(f"Pixels desenhados por g.fillRect(10, 10, 8, 5): {pixels_fillRect}")





