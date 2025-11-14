import pytest
import numpy as np
from src.CB2325NumericaG2.interpolacao import polinomial

# ---------- TESTES DOS COEFICIENTES ----------
@pytest.mark.parametrize(
    "x, y, esperado",
    [
        ([1,2], [1,1], [1,0]),
        ([1,2], [1,2], [0,1]),
        ([1,2,3], [1,2,4], [1,-0.5,0.5]),
        ([1,2,3,4], [17,4,71,202], [126,-162.33333333333,56,-2.66666666667]),
        ([1,2,-3,4,5,0],[-39,-368,-243,-3456,-6875,0], [0,0,0,-30,-10,1]),
        ([1, 2], [5, 7], [3,2]),
        ([0, 1, 2], [0, 1, 4], [0,0,1]),
        ([1, 5, 10], [10, 10, 10], [10,0,0]),
        ([3], [99], [99]),
        ([-1, 0, 1, 2], [0, 0, 0, 6], [0,-1,0,1]),
        ([-2, 0, 2], [4, 0, 4], [0,0,1]),
        ([3, 1], [10, 4], [1,3]),
        ([0, 1, 2, 3, 4], [1, 2, 5, 10, 17], [1,0,1,0,0]),
        ([],[],[])
    ]
)
def test_coeficientes_polinomio(x, y, esperado):
    resultado = polinomial(x, y)
    assert resultado.coeficientes() == pytest.approx(esperado, abs=1e-9)

# ---------- TESTES DOS PONTOS ORIGINAIS ----------
@pytest.mark.parametrize(
    "x, y",
    [
        ([1,2], [1,1]),
        ([1,2], [1,2]),
        ([1,2,3], [1,2,4]),
        ([1,2,3,4], [17,4,71,202]),
        ([1,2,-3,4,5,0],[-39,-368,-243,-3456,-6875,0]),
        ([1, 2], [5, 7]),
        ([0, 1, 2], [0, 1, 4]),
        ([1, 5, 10], [10, 10, 10]),
        ([3], [99]),
        ([-1, 0, 1, 2], [0, 0, 0, 6]),
        ([-2, 0, 2], [4, 0, 4]),
        ([3, 1], [10, 4]),
        ([0, 1, 2, 3, 4], [1, 2, 5, 10, 17])
    ]
)
def test_pontos_originais(x, y):
    resultado = polinomial(x, y)
    assert resultado(x) == pytest.approx(y, abs=1e-9)


# ---------- TESTES DA AVALIAÇÃO DE NOVOS PONTOS ----------
@pytest.mark.parametrize(
    "x, y, esperado",
    [
        ([1,2], [1,1], 1),
        ([1,2], [1,2], 2),
        ([1,2,3], [1,2,4], 2),
        ([1,2,3,4], [17,4,71,202], 4),
        ([1,2,-3,4,5,0],[-39,-368,-243,-3456,-6875,0], -368),
        ([1, 2], [5, 7], 7),
        ([0, 1, 2], [0, 1, 4], 4),
        ([1, 5, 10], [10, 10, 10], 10),
        ([3], [99], 99),
        ([-1, 0, 1, 2], [0, 0, 0, 6], 6),
        ([-2, 0, 2], [4, 0, 4], 4),
        ([3, 1], [10, 4], 7),
        ([0, 1, 2, 3, 4], [1, 2, 5, 10, 17], 5)
    ]
)
def test_novo_ponto(x, y, esperado):
    resultado = polinomial(x, y)
    assert resultado(2) == pytest.approx(esperado, abs=1e-9)

@pytest.mark.parametrize(
    "x, y, esperado",
    [
        ([1,2], [1,1], [1,1,1,1]),
        ([1,2], [1,2], [2,0.5,0,-1]),
        ([1,2,3], [1,2,4], [2,0.875,1,2]),
        ([1,2,3,4], [17,4,71,202], [4,58.5,126,347]),
        ([1,2,-3,4,5,0],[-39,-368,-243,-3456,-6875,0], [-368,-4.34375,0,19]),
        ([0, 1, 2], [0, 1, 4], [4,0.25,0,1]),
        ([1, 5, 10], [10, 10, 10], [10,10,10,10]),
        ([3], [99], [99,99,99,99]),
        ([-1, 0, 1, 2], [0, 0, 0, 6], [6,-0.375,0,0])
    ]
)
def test_lista_novos_pontos(x, y, esperado):
    resultado = polinomial(x, y)
    assert resultado([2,0.5,0,-1]) == pytest.approx(esperado, abs=1e-9)

# ---------- TESTES DE ERROS ----------

def test_erro_tamanhos_diferentes():
    with pytest.raises(ValueError):
        p = polinomial([1, 2, 3], [1, 2])
        p.coeficientes()

def test_erro_vandermonde_singular():
    # x repetidos
    p = polinomial([1, 1, 2], [1, 2, 3])
    with pytest.raises(np.linalg.LinAlgError):
        p.coeficientes()

def test_erro_tipo_invalido_call():
    p = polinomial([0, 1], [0, 1])
    with pytest.raises(ValueError):
        p("texto")

def test_erro_lista_com_tipo_invalido_call():
    p = polinomial([0, 1], [0, 1])
    with pytest.raises(TypeError):
        p([0, "a", 2])
