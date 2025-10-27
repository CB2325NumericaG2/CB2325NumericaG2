from functools import reduce
from typing import Callable

def integral(func:Callable[[float],float], pi:float, pf:float, n:int) -> float:
    h = (pf-pi)/n
    pontos = [pi + h*i for i in range(n+1)]
    area = reduce(lambda acc, i: acc + (func(pontos[i])+func(pontos[i+1]))*h/2, range(n), 0)
    return area
    
# Teste
pi = -10
pf = 10
n=20
h = (pf-pi)/n
pontos = [pi]
for p in range(n):
    pontos += [pontos[p] + h]
   # print(pontos)
print(pontos)

f = lambda x, y: x**2 + y

print(integral(f,-10, 10, 20))
    