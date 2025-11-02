import numpy as np
import math

class PolinomioHermite:
    def __init__(self, D: list[tuple[float, ...]]):
        """Inicializa o Polinômio Interpolador de Hermite.
        
        Args:
            D: Lista de tuplas estruturada como (x,f(x),f'(x),...,f^k(x)).

        Raises:
            ValueError: Se os dados não existem ou se não houver x e f(x) para todos os
                        pontos informados.
        """
        if not D or not all(len(d) > 1 for d in D):
            raise ValueError
            
        self.data = D
        self.condicoes = sum(len(d) - 1 for d in D)
        self.grau = self.condicoes - 1
        
        self.x = np.zeros(self.condicoes)
        self.y = np.zeros(self.condicoes) 
        self.derivadas = {}
        indice = 0
        for tupla in D:
            x = tupla[0]
            derivadas = len(tupla) - 1
            for i in range(derivadas):
                self.x[indice + i] = x #x
                self.y[indice + i] = tupla[1] #f(x)
                self.derivadas[(x, i)] = tupla[1 + i] #derivadas
            indice += derivadas
        self.coeficientes = self.newton()
        
    def newton(self) -> np.ndarray:
        """Calcula os coeficientes do polinômio de Hermite pelo método de Newton de
           diferenças divididas."""
        
        # tabela de diferenças divididas
        d = np.zeros((self.condicoes, self.condicoes))
        d[:, 0] = self.y 
        
        for i in range(1, self.condicoes):
            for j in range(self.condicoes - i):
                if self.x[j] != self.x[j+i]:
                    # Regra de Newton
                    d[j, i] = (d[j+1, i-1] - d[j, i-1]) / (self.x[j+i] - self.x[j])
                else:
                    # f^(i)(x)/i!
                    x = self.x[j]
                    derivada = self.derivadas.get((x, i), 0.0) 
                    d[j, i] = derivada / math.factorial(i)
        return d[0]

    def __str__(self) -> str:
        """Representa em string o polinômio interpolador na forma de Newton."""
        if len(self.coeficientes) == 0:
            return "0"
        polinomio = f"({self.coeficientes[0]})" # c_0
        for i in range(1, self.condicoes):
            termo = f"({self.coeficientes[i]})" # c_i
            for j in range(i):
                termo += f"*(x-({self.x[j]}))"
            polinomio += f"+{termo}"
        return polinomio

    def avaliar(self, x: float|int) -> float:
        """Avalia o polinômio interpolador para o valor x.
        
        Args:
            x: Valor a ser interpolado.

        Returns:
            float: Resultado de x no polinômio interpolador.

        Raises:
            ValueError: Se x não é do tipo numérico 
        """
        if len(self.coeficientes) == 0:
            return 0
        polinomio = self.coeficientes[0] # c_0
        for i in range(1, self.condicoes):
            termo = self.coeficientes[i] # c_i
            for j in range(i):
                termo *=(x-self.x[j])
            polinomio += termo
        return polinomio
    
    def __call__(self, x: float|int|list[float|int]|np.ndarray) -> float|list[float]:
        """Permite que o polinômio atue como uma função matemática com entrada x.
        
        Args:
            x: Valor(es) a ser(em) interpolado(s).

        Returns:
            Resultado de x no polinômio interpolador.

        Raises:
            ValueError: Se x não é do tipo numérico.
        """
        if isinstance(x, (float, int, np.float64, np.float32, np.int64, np.int32)):
            return self.avaliar(float(x)) 
        elif isinstance(x, (list, np.ndarray)):
            resultados = [self.avaliar(float(i)) for i in x]
            return resultados
        raise ValueError
