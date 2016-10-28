import numpy
import math

n = int(raw_input('Entre com o valor de n\n'))
# monta uma matriz nxn aleatoria entre (-10,10)
a = numpy.random.random_integers(-10, 10, (n, n))

# monta a matriz x* = [1, 2, 3, ... , n]^T
x_in = numpy.empty((n,1), dtype=int)
for i in range(n):
	x_in[i][0] = i+1

# define b a partir de x_in (x*)
b = numpy.dot(a, x_in)

# resolve Ax = b
x = numpy.linalg.solve(a, b)

# calcula o residuo de x* (Rin) e x^ (Rout)		
Rin = numpy.linalg.norm(a*x_in - b)
Rout = numpy.linalg.norm(a*x - b)

# calcula a norma de x^ - x*
Dif = numpy.linalg.norm(x - x_in)

print Rin
print Rout
print Rin - Rout
print Dif
