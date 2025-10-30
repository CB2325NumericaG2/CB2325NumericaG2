import numpy as np
import matplotlib.pyplot as plt
import sympy

def riemann_integ_trapezio(f_string, a, b, n):

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

        # Definindo vertices do trapezio
        x_inicio = a + i * variacao
        y_inicio = f(x_inicio)

        x_fim = x_inicio + variacao
        y_fim = f(x_fim)

        x_vertices = [x_inicio, x_inicio, x_fim, x_fim]
        y_vertices = [0, y_inicio, y_fim, 0]
        
        # Calculando a area do trapezio e somando a area final
        area_trapezio = ((y_inicio + y_fim) * variacao) / 2
        area += area_trapezio
        
        # Preenchendo os trapézios 
        ax.fill(x_vertices, y_vertices, color='gray', edgecolor='black', alpha=0.5)



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
    ax.set_xlim([a, b])
    
    # Definindo os limites do gráfico
    min_y = min(0, np.min(y_curve)) 
    max_y = np.max(y_curve)
    ax.set_ylim([min_y - max_y*0.05, max_y * 1.1])
    
    plt.show()

# Teste
string = input('Digite a função:')
valor_a = input('Digite a:')
valor_b = input('Digite b:')
valor_n = input('Digite n:')

a_num = float(valor_a)
b_num = float(valor_b)
n_int = int(valor_n)
riemann_integ_trapezio(string, a_num, b_num, n_int)