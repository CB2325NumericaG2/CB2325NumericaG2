from typing import Sequence
from linear import interpolacao_linear

Vetor = list[float]

def interpolacao_linear_partes(
        x_valores: Sequence[float],
        y_valores: Sequence[float],
        x: float
        ) -> float:
    """
    Realiza interpolação linear por partes em R².

    Dado um conjunto de pontos (x_i, y_i), retorna o valor interpolado y(x)
    usando interpolação linear em cada intervalo [x_i, x_{i+1}].

    Args:
        pontos : sequência de pontos em R² (lista de listas ou tuplas)
        x : valor da variável independente onde se deseja interpolar

    Returns:
        float : valor interpolado de y em x.

    Raises:
        ValueError 
            - Se os pontos não estiverem em R²;
            - Se x estiver fora do intervalo;
    """

    if len(x_valores) != len(y_valores):
        raise ValueError("É necessário ter a mesma quantidade de valores de x e y.")

    if len(x_valores) < 2:
        raise ValueError("São necessários pelo menos dois pontos para interpolação linear por partes.")
    
    pontos = sorted(zip(x_valores, y_valores), key = lambda p: p[0])
    x_sorted, y_sorted = zip(*pontos)
    for p in pontos:
        if len(p) != 2:
            raise ValueError("Cada ponto deve ter duas coordenadas (x, y).")

    if not (x_sorted[0] <= x <= x_sorted[-1]):
        raise ValueError(f"x={x} está fora do intervalo [{x_valores[0]}, {x_valores[-1]}].")

    for i in range(len(x_sorted) - 1):
        x0, y0 = x_sorted[i], y_sorted[i]
        x1, y1 = x_sorted[i+1], y_sorted[i+1]
        if x0 == x1:
            raise ValueError(f'Pontos consecutivos com mesmo x = {x0} geram um segmento vertical: interpolação indefinida.')
        if x0 <= x <= x1:
            return interpolacao_linear([x0, y0], [x1, y1], x = x)
    
    raise RuntimeError("Erro interno: não foi encontrado o intervalo correspondente.")
