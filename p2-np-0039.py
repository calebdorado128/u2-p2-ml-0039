import numpy as np
# Caleb Dorado NC = 0039
# Ejemplos de Numpy, Numerical Python
print("-- Espacio Linealmente en Array -- 0039")
array=np.linspace(start=0, stop=5, num=5)
print(array)
print("-- Matrix Identidad en 2D Array -- 0039")
matrix=np.eye(3)
print(matrix)
print("-- Genera numeros al azar(Aleatorios) en 2D Array -- 0039")
numale=np.random.random((3,4)) # Genera 12 numeros aleatorios 
print(numale)
print("Genera 9 numeros aleatorios entre 0 y 1")
numale=np.random.random((3,3)) # Genera 9 numeros aleatorios 
print(numale)
# como generar 9 numeros aleatorios comprendidos entre 1 y 20 
# con numpy en un arreglo de 3 por 3
print("Genera 9 numeros aleatorios entre 1 y 20")
array = np.random.randint(1, 21, size=(3, 3))
print(array)
print("Caleb Dorado NC = 0039")
