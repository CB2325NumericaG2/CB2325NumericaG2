import matplotlib.pyplot as plt
import numpy as np

def minimos_quadrados(vetor_x : list,vetor_y : list) -> tuple:
    """
    Método de aproximação por minimos quadrados.  
    Retorna os coeficientes c, a e b da reta cy = ax + b
    a = numerador/denominador
    b = f(a)

    Args:
        vetor_x (list of float): Lista das abscissas.
        vetor_y (list of float): Lista das ordenadas.

    Returns:
        tuple:
            c (int): Indicador do tipo de reta. 
                     1 -> reta normal (y = a*x + b), 
                     0 -> reta vertical (x = b)
            a (float): Coeficiente angular da reta
            b (float): Coeficiente linear da reta 
    
    """
    #calculo do Denominador de a 
    somatorio_xi = 0
    somatorio_xi_ao_quadrado = 0
    for xi in vetor_x:
        somatorio_xi += xi
        somatorio_xi_ao_quadrado += xi**2
    n = len(vetor_x)
    denominador = (n*somatorio_xi_ao_quadrado) - (somatorio_xi**2)
    if denominador != 0:
        #calculo do numerador de a
        somatorio_xi_yi = 0
        somatorio_yi = 0
        for i in range(0,n):
            somatorio_yi += vetor_y[i]
            somatorio_xi_yi += vetor_x[i]*vetor_y[i]
        numerador = (n*somatorio_xi_yi) - (somatorio_xi*somatorio_yi)

        #calculo final de a
        a = numerador/denominador

        #calculo de b
        b = (somatorio_yi - a*somatorio_xi)/n

        return 1, a, b
    else: # Todos os x são iguais => Reta vertical 
        return 0, 1, vetor_x[0]

def theil_sen(x: list, y: list) -> tuple:
    """
    Estima y ≈ a + b x (Theil–Sen).
    Retorna: flag, a, b
      - flag = 0 -> reta vertical (todos x iguais): x = a, b = +inf (não usado)
      - flag = 1 -> reta não vertical: y = a + b x
    """
    x = np.asarray(x, float); y = np.asarray(y, float)
    if x.shape != y.shape:
        raise ValueError("x e y devem ter o mesmo tamanho.")
    n = x.size
    if n < 2:
        raise ValueError("É preciso ao menos dois pontos.")

    # Caso vertical: todos os x iguais
    if np.ptp(x) == 0.0:  # ptp = max(x) - min(x)
        x0 = float(np.median(x))
        return 0, x0, x[0]

    # Caso geral: ignora pares com dx == 0
    slopes = []
    for i in range(n - 1):
        dx = x[i+1:] - x[i]
        valid = dx != 0
        if np.any(valid):
            dy = y[i+1:] - y[i]
            slopes.extend((dy[valid] / dx[valid]).tolist())

    b = float(np.median(slopes))       # inclinação = mediana das inclinações
    a = float(np.median(y - b * x))    # intercepto = mediana dos resíduos
    return 1, a, b

def plot_linear_minimos_quadrados(x, y):
    """
    Plota os pontos fornecidos e a reta de ajuste linear por mínimos quadrados.

    A função calcula os coeficientes da reta que melhor se ajusta aos pontos (x, y)
    usando o método dos mínimos quadrados e plota tanto os pontos originais quanto 
    a reta ajustada. Caso todos os valores de x sejam iguais, plota-se uma reta 
    vertical correspondente.

    Args:
        x (list of float): Lista das abscissas dos pontos a serem plotados.
        y (list of float): Lista das ordenadas dos pontos a serem plotados.

    Returns:
        None
    """
    c, a, b = minimos_quadrados(x, y)

    plt.scatter(x, y, color='royalblue', label='Pontos reais')

    if c == 0:
        # reta vertical
        y_min, y_max = min(y), max(y)
        plt.vlines(b, y_min, y_max, color='crimson', linewidth=2,
                   label=f'Reta vertical: x = {b:.2f}')
        plt.title('Ajuste Linear - Reta Vertical (Mínimos Quadrados)')
    else:
        # reta normal
        x_min, x_max = min(x), max(x)
        x_fit = [x_min, x_max]
        y_fit = [a * x_min + b, a * x_max + b]
        plt.plot(x_fit, y_fit, color='crimson', linewidth=2,
                 label=f'Ajuste: y = {a:.2f}x + {b:.2f}')
        plt.title('Ajuste Linear por Mínimos Quadrados')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_linear_theil_sen(x, y):
    """
    Plota os pontos (x, y) e a reta de ajuste linear pelo método de Theil–Sen.

    Usa a função theil_sen(x, y) definida anteriormente, que retorna:
      flag, a, b
        - flag = 0 -> reta vertical (todos os x iguais): x = a
        - flag = 1 -> reta não vertical: y = a + b x

    Args:
        x (list[float] | np.ndarray): abscissas
        y (list[float] | np.ndarray): ordenadas
    """
    flag, a, b = theil_sen(x, y)

    # pontos
    plt.scatter(x, y, color='royalblue', label='Pontos reais')

    if flag == 0:
        # reta vertical x = a
        y_min, y_max = min(y), max(y)
        plt.vlines(a, y_min, y_max, color='crimson', linewidth=2,
                   label=f'Reta vertical: x = {a:.2f}')
        plt.title('Ajuste Linear - Reta Vertical (Theil–Sen)')
    else:
        # reta não vertical: y = a + b x
        x_min, x_max = min(x), max(x)
        x_fit = [x_min, x_max]
        y_fit = [a + b * x_min, a + b * x_max]
        plt.plot(x_fit, y_fit, color='crimson', linewidth=2,
                 label=f'Ajuste (Theil–Sen): y = {b:.2f}x + {a:.2f}')
        plt.title('Ajuste Linear por Theil–Sen')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()



if __name__ =="__main__":

    X1 = [5,7,8,7,2,17,2,9,4,11,12,9,6]
    Y1 = [1000,86,87,88,111,86,103,87,94,78,77,85,86]
    c, a, b = minimos_quadrados(X1,Y1)
    if c:
        print(f"y = {a:.2f}x + {b:.2f}")
    else: 
        print(f"x = {b:.2f}")
    plot_linear_minimos_quadrados(X1, Y1)

    # (corrigido) usar Theil–Sen aqui:
    c, a, b = theil_sen(X1,Y1)
    if c:
        print(f"y = {b:.2f}x + {a:.2f}")
    else: 
        print(f"x = {a:.2f}")
    plot_linear_theil_sen(X1, Y1)

    # reta vertical
    X2 = [3, 3, 3, 3]  
    Y2 = [1, 2, 3, 4] 
    c, a, b = minimos_quadrados(X2,Y2)
    if c:
        print(f"y = {a:.2f}x + {b:.2f}")
    else: 
        print(f"x = {b:.2f}")
    plot_linear_minimos_quadrados(X2, Y2)

    c, a, b = theil_sen(X2,Y2)
    if c:
        print(f"y = {b:.2f}x + {a:.2f}")
    else: 
        print(f"x = {a:.2f}")
    plot_linear_theil_sen(X2, Y2)
