import numpy as np

def poly_interp(x: list[float], y: list[float]) -> list[float]:
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

    #matriz de Vandermonde
    '''matrizV = []
    for i in x:
        linha = []
        for j in range(len(x)):
            linha.append(i**j)
        matrizV.append(linha.copy())'''
    matrizV = np.vander(x, increasing=True)
    X = np.linalg.solve(matrizV, y)
    return X.tolist()
    
if __name__ == "__main__":
    poly_interp([1,2], [1,1])==[1,0]
    poly_interp([1,2], [1,2])==[0,1]
    poly_interp([1,2,3], [1,2,4])==[1,-0.5,0.5]
    poly_interp([1,2,3,4], [17,4,71,202])==[126,-162.33333333,56,-2.66666667]
    poly_interp([1,2,-3,4,5,0],[-39,-368,-243,-3456,-6875,0])==[1,-30,-10]
    poly_interp([1, 2], [5, 7])==[3,2]
    poly_interp([0, 1, 2], [0, 1, 4])==[0,0,1]
    poly_interp([1, 5, 10], [10, 10, 10])==[10,0,0]
    poly_interp([3], [99])==[99]
    poly_interp([-1, 0, 1, 2], [0, 0, 0, 6])==[0,-1,0,1]
    poly_interp([-2, 0, 2], [4, 0, 4])==[0,0,1]
    poly_interp([3, 1], [10, 4])==[1,3]
    poly_interp([0, 1, 2, 3, 4], [1, 2, 5, 10, 17])==[1,0,1,0,0]

'''poly_interp([1,2], [1,1]) #f(x)=1 [1,0]
poly_interp([1,2], [1,2]) #f(x)=x [0,1]
poly_interp([1,2,3], [1,2,4]) #f(x)=0.5x^2-0.5x+1 [1,-0.5,0.5]
poly_interp([1,2,3,4], [17,4,71,202]) #f(x)=-2.66666667x^3+56x^2-162.33333333x+126 [126,-162.33333333,56,-2.66666667]
poly_interp([1,2,-3,4,5,0],[-39,-368,-243,-3456,-6875,0]) #f(x)=-10x^5-30x^4+x^3
poly_interp([1, 2], [5, 7]) #[3,2]
poly_interp([0, 1, 2], [0, 1, 4]) #[0,0,1]
poly_interp([1, 5, 10], [10, 10, 10]) #[10,0,0]
poly_interp([3], [99]) #[99]
poly_interp([-1, 0, 1, 2], [0, 0, 0, 6]) #[0,-1,0,1]
poly_interp([-2, 0, 2], [4, 0, 4]) #[0,0,1]
poly_interp([3, 1], [10, 4]) #[1,3]
poly_interp([0, 1, 2, 3, 4], [1, 2, 5, 10, 17]) #[1,0,1,0,0]'''