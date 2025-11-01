from src.erros_numericos.erro_absoluto import erro_Absoluto
import pytest

def test_numeros_positivos():
    assert erro_Absoluto(5, 3) == 2
    
def test_ordem_invertida():
    assert erro_Absoluto(3, 5) == 2
        
def test_com_numeros_negativos():
    assert erro_Absoluto(-5, -10) == 5
        
def test_positivo_e_negativo():
    assert erro_Absoluto(10, -10) == 20

def test_numeros_identicos():
    assert erro_Absoluto(7, 7) == 0

def test_com_zero():
    assert erro_Absoluto(15, 0) == 15
        
def test_caso_do_usuario_com_floats():
    # 'pytest.approx' é a forma do pytest de lidar com floats
    assert erro_Absoluto(3.1415, 3.14) == pytest.approx(0.0015)

# Não precisa do 'if __name__ == "__main__"'