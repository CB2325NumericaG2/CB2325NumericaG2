from src.erro_numericos_julia import erro_relativo

def func(x):
    return x +1

def test_answer():
    assert func(3) == 4


'''valor de π
    valor_real_pi = 3.141592
    valor_aproximado_pi = 3.14

    valor de e
    valor_real_e = 2.718282
    valor_aproximado_e = 2.72

    valor de √2
    valor_real_raiz2 = 1.414214
    valor_aproximado_raiz2 = 1.41

    valor da gravidade
    valor_real_g = 9.806650
    valor_aproximado_g = 9.81'''

def test_erro_relativo():
    assert erro_relativo(3.141592, 3.14) == 0.0005067