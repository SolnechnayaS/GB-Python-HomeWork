print('5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.')
xa = float(input('Точка А (x) = '))
ya = float(input('Точка А (y) = '))
xb = float(input('Точка B (x) = '))
yb = float(input('Точка B (y) = '))
distance = (((xb-xa)**2) + ((yb-ya)**2))**0.5
print(f'Расстояние между двумя точками {round(distance, 4)}')