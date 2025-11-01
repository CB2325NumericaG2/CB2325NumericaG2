import numpy as np
import matplotlib.pyplot as plt
import sympy

x_simbolico = sympy.symbols('x')

def usuario() -> None:
    '''
    Solicita inserção de função, ponto de início, ponto de fim, número de subintervalos e parâmetro de altura ao usuário.
    Converte os inputs recebidos em tipos adequados aos parâmetros das funções.
    Chama a função metodo_retangulo para calculo da integral.
    Chama a função plote_grafico para visualização gráfica do método.
    '''
    string = input('Digite a função:')
    valor_a = input('Digite a:')
    valor_b = input('Digite b:')
    valor_n = input('Digite n:')
    valor_corte = input('Digite 0 para Soma de Riemann pela Esquerda,' \
                                '1 para Soma de Riemann pela Direita,'  \
                                '0.5 para Soma de Riemann pelo Centro:')
    
    a_num = float(valor_a)
    b_num = float(valor_b)
    n_int = int(valor_n)
    corte_num = float(valor_corte)

    area = metodo_retangulo(string, a_num, b_num, n_int, corte_num)
    print(area)
    
    plote_grafico(string, a_num, b_num, n_int, corte_num)

def metodo_retangulo(f_string: str, a: float, b: float, n: int, ponto_corte: float) -> float:
    '''
    Entradas:
    f_string - expressão algébrica
    a - ponto inicial do intervalo
    b - ponto final do intervalo
    n - número de subintervalos da partição
    ponto_corte - parâmetro de altura do subintervalo

    Saída: Integral aproximada pela Soma de Riemann com método dos retângulos
    '''
    expr_simbolica = sympy.sympify(f_string)
    f = sympy.lambdify(x_simbolico, expr_simbolica, 'numpy')

    variacao = (b - a) / n  
    area = 0

    for i in range(n):
        x_inicio = a + i * variacao
        y_inicio = f(x_inicio)
        x_fim = x_inicio + variacao
        y_fim = f(x_fim)

        x_altura = x_inicio + ponto_corte * (x_fim - x_inicio)
        y_altura = f(x_altura)
       
        area_retangulo = y_altura * variacao
        area += area_retangulo
    return area


def plote_grafico(f_string: str, a: float, b: float, n: int, ponto_corte: float) -> None:
    '''
    Entradas:
    f_string - expressão algébrica
    a - ponto inicial do intervalo
    b - ponto final do intervalo
    n - numero de subintervalos da partição
    ponto_corte - parametro de altura do subintervalo

    Saída: Gráfico de f com os retângulos da soma de Riemann
    '''
    expr_simbolica = sympy.sympify(f_string)
    f = sympy.lambdify(x_simbolico, expr_simbolica, 'numpy')

    plt.figure(figsize=(10, 6))
    ax = plt.gca()

    variacao = (b - a) / n  

    for i in range(n):
        x_inicio = a + i * variacao
        x_fim = x_inicio + variacao

        x_altura = x_inicio + ponto_corte * (x_fim - x_inicio)
        y_altura = f(x_altura)
       
        ax.bar(x_inicio, y_altura, width = variacao, align = 'edge', \
                color = 'gray', edgecolor = 'black', alpha = 0.5)

    area = metodo_retangulo(f_string, a, b, n, ponto_corte)

    x_curve = np.linspace(a, b, 400)
    y_curve = f(x_curve)
    ax.plot(x_curve, y_curve, color='black', linewidth=0.5, label=f'f(x) = {f_string}')
   
    ax.set_title(f"Método dos Trapézios (n={n}) | Área Aprox. = {area:.2f}")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()
    ax.grid(False)
   
    min_y = min(0, np.min(y_curve))
    max_y = np.max(y_curve)
    ax.set_xlim([a, b])
    ax.set_ylim([min_y - max_y*0.05, max_y * 1.1])
   
    plt.show()
