import numpy as np

class PolinomioInterpolador:
    def __init__(self,x:list[float],y:list[float]):
        """Inicializa o polinômio interpolador de um dado conjuto de pontos.

        Args:
            x: Coordenadas x dos pontos de interpolação. Pode ser uma lista ou array numpy.
            y: Coordenadas y dos pontos de interpolação. Pode ser uma lista ou array numpy.
        
        """
        self.x=np.array(x)
        self.y=np.array(y)
        self.coeficientes=self._coeficientes()

    def _coeficientes(self) -> list[float]:
        """Retorna os coeficientes do polinômio interpolador de grau n-1.

        O método calcula os coeficientes do polinômio interpolador que passa pelos
        pontos (x,y) por meio da construção da matriz de Vandermonde V e resolvendo o
        sistema linear V.X=y.
        O polinômio resultante é P(t) = X[0] + X[1]*t + ... + X[n-1]*t^(n-1).

        Returns:
            np.array: Coeficientes do polinômio do grau 0 ao grau n-1.

        Raises:
            numpy.linalg.LinAlgError: Se a matriz de Vandermonde for singular
            ValueError: Se as listas x e y tiverem tamanhos diferentes.
        """
        matrizV = np.vander(self.x, increasing=True)
        X = np.linalg.solve(matrizV, self.y)
        return X

    def __str__(self):
        """Representa o polinômio interpolador em formato de string.

        Returns:
            str: Representação no formato (a_0*x^0)+(a_1*x^1)+...+(a_n*x^n)
        """
        if len(self.coeficientes)==0:
            return "0"
        polinomio = f"({self.coeficientes[0]}*x^0)"
        for i in range(1,len(self.coeficientes)):
            polinomio="".join([polinomio,f"+({self.coeficientes[i]}*x^{i})"])
        return polinomio
    
    def __repr__(self):
        return self.coeficientes.tolist()
    
    def interpolacao(self, x):
        """Avalia o polinômio interpolador no valor de x.

        Args:
            x: O(s) ponto(s) onde o polinômio deve ser avaliado. 

        Returns:
            float: O resultado da avaliação do polinômio.
        """
        x = np.array(x)
        invertido = self.coeficientes[::-1]
        resultado = np.polyval(invertido, x)
        return resultado


polinomio = PolinomioInterpolador([1,2,-3,4,5,0],[-39,-368,-243,-3456,-6875,0])
print(polinomio)
print(PolinomioInterpolador.interpolacao(polinomio,2))
print(PolinomioInterpolador.interpolacao(polinomio,1))
print(PolinomioInterpolador.interpolacao(polinomio,[2,1]))
print(polinomio.__repr__())