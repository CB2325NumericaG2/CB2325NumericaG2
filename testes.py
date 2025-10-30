import pytest
import numpy as np
from Integracao_Numerica import integral

# ---------- TESTES DE FUNCIONALIDADE ----------

def test_integral_regra_trapezio():
    """Verifica se a integral de sin²(x) em [0, π] ≈ π/2"""
    f = lambda x: np.sin(x)**2
    result = integral(f, 0, np.pi, 100)
    expected = np.pi / 2
    assert np.isclose(result, expected, atol=1e-3)


# ---------- TESTES DE ERROS E TIPOS ----------

def test_tipo_errado_func():
    """Erro se 'func' não for chamável"""
    with pytest.raises(TypeError):
        integral(123, 0, 1, 10)


def test_tipo_errado_pi_pf():
    """Erro se pi/pf não forem floats"""
    with pytest.raises(TypeError):
        integral(lambda x: x, "a", 2, 10)


def test_tipo_errado_n():
    """Erro se n não for inteiro"""
    with pytest.raises(TypeError):
        integral(lambda x: x, 0, 1, 2.5)
