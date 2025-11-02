from typing import Callable, Sequence

def integral_retangulo(func:Callable[[float],float], a: float, b: float, n: int, ponto_corte:float = 0) -> float:
    '''
    Entradas:
    f_string - expressão algébrica
    a - ponto inicial do intervalo
    b - ponto final do intervalo
    n - número de subintervalos da partição
    ponto_corte - parâmetro de altura do subintervalo, recebe:
        - 0 para Soma de Riemann pela Esquerda
        - 1 para Soma de Riemann pela Direita
        - 0.5 para Soma de Riemann pelo Centro

    Saída: Integral aproximada pela Soma de Riemann com método dos retângulos
    '''
    
    variacao = (b - a) / n  
    area = 0

    for i in range(n):
        x_inicio = a + i * variacao
        x_fim = x_inicio + variacao

        x_altura = x_inicio + ponto_corte * (x_fim - x_inicio)
        y_altura = func(x_altura)
       
        area_retangulo = y_altura * variacao
        area += area_retangulo
    return area

def integral_componentes(
    f_vec: Callable[[float], Sequence[float]],
    a: float,
    b: float,
    n: int,
    ponto_corte: float
) -> tuple[float, ...]:
    '''
    Args:
    f_vec - função vetorial f(x) que retorna uma sequência numérica (tupla ou lista)
            Exemplo: lambda x: (x**2, x**3)
    a - ponto inicial do intervalo
    b - ponto final do intervalo
    n - número de subintervalos da partição
    ponto_corte - parâmetro de altura do subintervalo, recebe:
        - 0   -> Soma de Riemann pela Esquerda
        - 1   -> Soma de Riemann pela Direita
        - 0.5 -> Soma de Riemann pelo Centro

    Returns:
    Tupla com as integrais aproximadas (uma por componente)
    '''
    # Avalia a função uma vez para saber quantas componentes ela tem
    exemplo = f_vec(a)
    if not isinstance(exemplo, (tuple, list)):
        raise TypeError("A função vetorial deve retornar uma tupla ou lista numérica.")

    areas = []
    for i in range(len(exemplo)):
        # Cria função para o i-ésimo componente
        componente_i = lambda x, i=i: f_vec(x)[i]
        area_i = integral_retangulo(componente_i, a, b, n, ponto_corte)
        areas.append(area_i)

    return tuple(areas)
  
# Teste unitário

if __name__ == "__main__":
  f = lambda x: (x**2, x**3, x)
  resultado = integral_componentes(f, 0, 2, 100, 0.5)
  print(resultado)
