import numpy as np
import matplotlib.pyplot as plt
import sympy

def riemann_integ_trapezio(f_string, a, b, n, ponto_corte):

    # Definição de x para computação simbólica
    x_simbolico = sympy.symbols('x') 

    # Convertendo string em função
    expr_simbolica = sympy.sympify(f_string)
    f = sympy.lambdify(x_simbolico, expr_simbolica, 'numpy')

    # Inicio do plote da figura com definicao de eixos
    plt.figure(figsize=(10, 6))
    ax = plt.gca()
    
    # Subdividindo o intervalo do dominio
    variacao = (b - a) / n  

    area = 0
    for i in range(n):

        # Definindo vertices do retangulo
        x_inicio = a + i * variacao
        y_inicio = f(x_inicio)
        x_fim = x_inicio + variacao
        y_fim = f(x_fim)

        # Definindo altura do retângulo
        x_altura = x_inicio + ponto_corte * (x_fim - x_inicio)
        y_altura = f(x_altura)
        
        # Calculando a area do retangulo e somando a area final
        area_retangulo = y_altura * variacao
        area += area_retangulo
        
        # Preenchendo os trapézios 
        ax.bar(x_inicio, y_altura, width = variacao, align = 'edge', \
                color = 'gray', edgecolor = 'black', alpha = 0.5)



    # Plotando a curva da função
    x_curve = np.linspace(a, b, 400)
    y_curve = f(x_curve)
    ax.plot(x_curve, y_curve, color='black', linewidth=0.5, label=f'f(x) = {f_string}')
    
    # Plotando elementos na figura
    ax.set_title(f"Método dos Trapézios (n={n}) | Área Aprox. = {area:.2f}")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()
    ax.grid(False)
    
    # Definindo os limites do gráfico
    min_y = min(0, np.min(y_curve)) 
    max_y = np.max(y_curve)
    ax.set_xlim([a, b])
    ax.set_ylim([min_y - max_y*0.05, max_y * 1.1])
    
    plt.show()

# Teste
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

riemann_integ_trapezio(string, a_num, b_num, n_int, corte_num)