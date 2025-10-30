import matplotlib.pyplot as plt
import numpy as np
from functools import reduce
from typing import Callable

def integral_trapézio(func:Callable[[float],float], pi:float, pf:float, n:int, plot:bool=False) -> float:
    """
    Aplica o método da Regra do Trapézio Composta para encontrar uma aproximação da integral de f(x) 
    no intervalo [pi, pf]. Para isso, o intervalo é dividido em n subintervalos de tamanho igual e em cada 
    deles é construído um trapézio que aproximará a área sob o gráfico de f(x) naquela parte.

    Args:
        func (Callable[[float], float]): Função f(x).
        pi (float): Limite inferior do intervalo.
        pf (float): Limite superior do intervalo.
        n (int): Número de subdivisões trapezoidais.
        plot (float, opcional): Visualização do gráfico de f(x) com n subdivisões trapezoidais e a área sombreada.

    Returns:
        float: Aproximação da integral de f(x) = 0.

    Raises:
        TypeError: Se um dos seguintes casos ocorrer:
            - func não for uma função chamável 
            - pi e pf não forem float 
            - n não for inteiro           
    """
    if not callable(func):
        raise TypeError("'func' deve ser uma função chamável")
    if not isinstance(pi, (int, float)) or not isinstance(pf, (int, float)):
        raise TypeError("'pi' e 'pf' devem ser números (int ou float)")
    if not isinstance(n, int):
        raise TypeError("'n' deve ser um inteiro")
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

        plt.title(f"Método dos Trapézios (n={n}) | Área Aprox. = {area:.2f}")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.grid(True)
        plt.show()
    return area

# Teste unitário
if __name__ == "__main__":
    f = lambda x: np.sin(x)**2
    resultado = integral_trapézio(f, -10, 10, 50, plot=True)
    print(f"Integral aproximada = {resultado}")
