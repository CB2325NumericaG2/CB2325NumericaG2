import pytest
from src.interpolacao import Interpolacao

print(Interpolacao)

print("Hello world!")
@pytest.mark.parametrize(
    "a, b, t, esperado",
    [
        ([2, 4], [6, 12], 0,   [2.0, 4.0]),
        ([2, 4], [6, 12], 0.5, [4.0, 8.0]),
        ([2, 4], [6, 12], 1,   [6.0, 12.0]),
    ]
)
def test_linear_parametrico(a, b, t, esperado):
    resultado = Interpolacao.linear(a, b, t=t)
    assert resultado == esperado
