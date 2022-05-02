# coding: utf-8

import numpy as np
import matplotlib.pylab as plt

def SierpinskiTriangulo(a, b, c, iteracoes):
    '''
    Função Recusiva que gera o Triangulo de Sierpinski. 
    '''
    if iteracoes == 0:
        # Preenche o triangulo com os vertices a, b, c. 
        plt.fill([a[0], b[0], c[0]], [a[1], b[1], c[1]], 'g') 
    else:
        # Recusão chama por outros triangulos. 
        SierpinskiTriangulo(a, (a + b) / 2., (a + c) / 2., iteracoes - 1) 
        SierpinskiTriangulo(b, (b + a) / 2., (b + c) / 2., iteracoes - 1) 
        SierpinskiTriangulo(c, (c + a) / 2., (c + b) / 2., iteracoes - 1)
        
a = np.array([0, 0])
b = np.array([1, 0])
c = np.array([0.5, np.sqrt(3)/2.])

iteracoes = 0

fig = plt.figure(figsize=(15,15))
plt.subplot(2,3,1).set_title("Sierpinski Triangulo (iteracoes = 0)")

SierpinskiTriangulo(a, b, c, iteracoes)

plt.axis('equal')
plt.axis('off')

iteracoes = 1

plt.subplot(2,3,2).set_title("Sierpinski Triangulo (iteracoes = 1)")

SierpinskiTriangulo(a, b, c, iteracoes)

plt.axis('equal')
plt.axis('off')

iteracoes = 2

plt.subplot(2,3,3).set_title("Sierpinski Triangulo (iteracoes = 2)")

SierpinskiTriangulo(a, b, c, iteracoes)

plt.axis('equal')
plt.axis('off')

iteracoes = 3

plt.subplot(2,3,4).set_title("Sierpinski Triangulo (iteracoes = 3)")

SierpinskiTriangulo(a, b, c, iteracoes)

plt.axis('equal')
plt.axis('off')

iteracoes = 4

plt.subplot(2,3,5).set_title("Sierpinski Triangulo (iteracoes = 4)")

SierpinskiTriangulo(a, b, c, iteracoes)

plt.axis('equal')
plt.axis('off')

iteracoes = 5

plt.subplot(2,3,6).set_title("Sierpinski Triangulo (iteracoes = 5)")

SierpinskiTriangulo(a, b, c, iteracoes)

plt.axis('equal')
plt.axis('off')

iteracoes = 6

plt.figure(figsize=(25,25))

SierpinskiTriangulo(a, b, c, iteracoes)

plt.title("Sierpinski Triangulo (iteracoes = 6)")
plt.axis('equal')
plt.axis('off')
plt.show()