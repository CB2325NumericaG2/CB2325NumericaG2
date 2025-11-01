import pytest
import numpy as np
from integracao_numerica.integracao_trapezios import integral_trapézio
from integracao_numerica.integracao_retangulos import integral_retangulo

# ---------- TESTES DE FUNCIONALIDADE ----------

def test_integral_regra_trapezio():
    """Verifica se a integral de sin²(x) em [0, π] ≈ π/2"""
    f = lambda x: np.sin(x)**2
    result = integral_trapézio(f, 0, np.pi, 100)
    expected = np.pi / 2
    assert np.isclose(result, expected, atol=1e-3)

def test_integral_regra_retangulo():
    """Verifica se a integral de sin²(x) em [0, π] ≈ π/2"""
    f = lambda x: np.sin(x)**2
    result = integral_retangulo(f, 0, np.pi, 100, 0)
    expected = np.pi / 2
    assert np.isclose(result, expected, atol=1e-3)


# ---------- TESTES DE ERROS E TIPOS ----------

# ----------  Método dos Trapézios ---------- 

def test_tipo_errado_func():
    """Erro se 'func' não for chamável"""
    with pytest.raises(TypeError):
        integral_trapézio(123, 0, 1, 10)

def test_tipo_errado_pi_pf():
    """Erro se pi/pf não forem floats"""
    with pytest.raises(TypeError):
        integral_trapézio(lambda x: x, "a", 2, 10)

def test_tipo_errado_n():
    """Erro se n não for inteiro"""
    with pytest.raises(TypeError):
        integral_trapézio(lambda x: x, 0, 1, 2.5)

# ----------  Método dos Retângulos ---------- 
       
def test_tipo_errado_func2():
    """Erro se 'func' não for chamável"""
    with pytest.raises(TypeError):
        integral_retangulo(123, 0, 1, 10)

def test_tipo_errado_pi_pf2():
    """Erro se pi/pf não forem floats"""
    with pytest.raises(TypeError):
        integral_retangulo(lambda x: x, "a", 2, 10)

def test_tipo_errado_n2():
    """Erro se n não for inteiro"""
    with pytest.raises(TypeError):
        integral_retangulo(lambda x: x, 0, 1, 2.5)

