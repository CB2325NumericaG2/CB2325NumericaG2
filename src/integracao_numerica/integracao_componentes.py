import integracao_retangulos as integr
import sympy

x_simbolico = sympy.symbols('x')

def integracao_componentes(f_string: str, a: float, b: float, n: int, ponto_corte: float) -> tuple:
    '''
    Entradas: 
    f_string - string com os componentes da curva em formato de tupla
    a - ponto inicial do intervalo
    b - ponto final do intervalo
    n - número de subintervalos da partição
    ponto_corte - parâmetro de altura do subintervalo

    Saída: Integral aproximada pela Soma de Riemann com método dos retângulos de cada componente da curva
    '''
    expr_simbolicas = sympy.sympify(f_string) 
    areas = []
    for componente in expr_simbolicas:
      area = integr.integral_retangulo(componente, a, b, n, ponto_corte)
      areas.append(area)
    tupla_areas = tuple(areas)
    return tupla_areas

def usuario() -> None:
    '''
    Solicita inserção de função, ponto de início, ponto de fim, número de subintervalos e parâmetro de altura ao usuário.
    Converte os inputs recebidos em tipos adequados aos parâmetros das funções.
    Chama a função integração_componente para cálculo da integral de cada componente
    '''
    string = input('Digite a função:')
    valor_a = input('Digite o ponto inicial da integração:')
    valor_b = input('Digite o ponto final da integração:')
    valor_n = input('Digite o valor de subintervalos da integração por componentes:')
    valor_corte = input('Digite 0 para Soma de Riemann pela Esquerda,' \
                                '1 para Soma de Riemann pela Direita,'  \
                                '0.5 para Soma de Riemann pelo Centro:')
    
    a_num = float(valor_a)
    b_num = float(valor_b)
    n_int = int(valor_n)
    corte_num = float(valor_corte)

    print(integracao_componentes(string, a_num, b_num, n_int, corte_num))