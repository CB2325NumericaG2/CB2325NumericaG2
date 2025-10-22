import matplotlib.pyplot as plt

def aproximacao_linear_por_minimos_quadrados(vetor_x : list,vetor_y : list):
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

        return 1, a, b  #Tem que falar com o emílio pra reajustar a saída.
    else: # Todos os x são iguais => Reta vertical 
        return 0, 1, vetor_x[0]  #Tem que falar com o emílio pra reajustar a sáida.

def plot_linear(x, y):
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
    c, a, b = aproximacao_linear_por_minimos_quadrados(x, y)

    plt.scatter(x, y, color='royalblue', label='Pontos reais')

    if c == 0:
        # reta vertical
        y_min, y_max = min(y), max(y)
        plt.vlines(b, y_min, y_max, color='crimson', linewidth=2,
                   label=f'Reta vertical: x = {b:.2f}')
        plt.title('Ajuste Linear - Reta Vertical')
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


if __name__ =="__main__":

    X1 = [1, 2, 3, 4, 5]
    Y1 = [2.2, 2.8, 4.5, 3.7, 5.5]
    c, a, b = aproximacao_linear_por_minimos_quadrados(X1,Y1)
    if c:
        print(f"y = {a:.2f}x + {b:.2f}")
    else: 
        print(f"x = {b:.2f}")
    plot_linear(X1, Y1)

    # reta vertical
    X2 = [3, 3, 3, 3]  
    Y2 = [1, 2, 3, 4] 
    c, a, b = aproximacao_linear_por_minimos_quadrados(X2,Y2)
    if c:
        print(f"y = {a:.2f}x + {b:.2f}")
    else: 
        print(f"x = {b:.2f}")
    plot_linear(X2, Y2)
