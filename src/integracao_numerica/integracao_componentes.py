import integracao_retangulos as int
import sympy

def integracao_componentes(f_string, a, b, n, ponto_corte):
    expr_simbolicas = sympy.sympify(f_string) 
    areas = []
    for componente in expr_simbolicas:
      area = int.metodo_retangulo(componente, a, b, n, ponto_corte)
      areas.append(area)
    tupla_areas = tuple(areas)
    return tupla_areas

# Teste unitário 

print(integracao_componentes("(x**2, x**3)", 1, 10, 5, 0.5))