import numpy as np

def interp_poli(x: list[float], y: list[float]) -> list[float]:
    """Retorna os coeficientes do polinômio interpolador de grau n-1.

    O método calcula os coeficientes do polinômio interpolador que passa pelos
    pontos (x,y) por meio da construção da matriz de Vandermonde V e resolvendo o
    sistema linear V.X=y.
    O polinômio resultante é P(t) = X[0] + X[1]*t + ... + X[n-1]*t^(n-1).

    Args:
        x (list[float]): Coordenadas x dos pontos de interpolação.
        y (list[float]): Coordenadas y dos pontos de interpolação.

    Returns:
        list[float]: Coeficientes do polinômio do grau 0 ao grau n-1.

    Raises:
        numpy.linalg.LinAlgError: Se a matriz de Vandermonde for singular
        ValueError: Se as listas x e y tiverem tamanhos diferentes.
    """
    matrizV = np.vander(x, increasing=True)
    X = np.linalg.solve(matrizV, y)
    return X.tolist()
