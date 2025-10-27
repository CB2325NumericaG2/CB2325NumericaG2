import pytest
import math
from . import bissecao, newton_raphson, secante  

def test_bissecao():
    f = lambda x: x**2 - 2
    aproximacao = bissecao(f, 1, 2, tol=1e-7, max_iter=100)
    assert abs(aproximacao - math.sqrt(2)) < 1e-7

def test_newton_raphson():
    f = lambda x: x**2 - 2
    df = lambda x: 2*x
    aproximacao = newton_raphson(f, df, x0=1, tol=1e-7, max_iter=100)
    assert abs(aproximacao - math.sqrt(2)) < 1e-7

def test_secante():
    f = lambda x: x**2 - 2
    aproximacao = secante(f, x0=1, x1=2, tol=1e-7, max_iter=100)
    assert abs(aproximacao - math.sqrt(2)) < 1e-7


if __name__ == "__main__":
    pytest.main()
