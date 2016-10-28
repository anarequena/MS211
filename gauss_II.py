import numpy
import math
from scipy.linalg import hilbert

n = int(raw_input('Entre com o valor de n\n'))
# cria a matriz de Hilbert
a = hilbert(n)

# cria x* = (1, 1, ... , 1)
x_in = []
linha = []
for j in range(1):
	linha.append(1)
for i in range(n):
	x_in.append(linha)
		
# define b a partir de x_in (x*)
b = numpy.dot(a, x_in)

# resolve Ax = b
x = numpy.linalg.solve(a, b)

# calcula o residuo de x* (Rin) e x^ (Rout)		
Rin = numpy.linalg.norm(a*x_in - b)
Rout = numpy.linalg.norm(a*x - b)

Dif = numpy.linalg.norm(x - x_in)

print Rin
print Rout
print Rin - Rout
print Dif
