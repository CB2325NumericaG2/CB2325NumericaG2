import matplotlib.pyplot as plt
import numpy as np
from functools import reduce
from typing import Callable

def integral(func:Callable[[float],float], pi:float, pf:float, n:int, plot:bool=False) -> float:
    h = (pf - pi) / n
    pontos = [pi + h*i for i in range(n+1)]
    
    # Cálculo da integral com regra do trapézio
    area = reduce(lambda acc, i: acc + (func(pontos[i]) + func(pontos[i+1])) * h / 2, range(n), 0)

    # Plotagem (opcional)
    if plot:
        # Gerar pontos para desenhar a curva da função
        x = np.linspace(pi, pf, 400)
        y = func(x)

        plt.figure(figsize=(10,6))
        plt.plot(x, y, 'b', label='f(x)')  # Curva da função
        plt.axhline(0, color='black', linewidth=1)

        # Desenhar trapézios
        for i in range(n):
            x_trap = [pontos[i], pontos[i], pontos[i+1], pontos[i+1]]
            y_trap = [0, func(pontos[i]), func(pontos[i+1]), 0]
            plt.fill(x_trap, y_trap, 'orange', alpha=0.3, edgecolor='r')

        plt.title(f"Regra do Trapézio Composta com n={n}")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.grid(True)
        plt.show()

    return area


# Teste
f = lambda x: np.sin(x)**2
resultado = integral(f, -10, 10, 50, plot=True)
print(f"Integral aproximada = {resultado}")
