def erro_relativo(valor_real, valor_aproximado):
    ''' calcula o erro do valor aproximado em
    proporção ao valor real,retornando a divisao
    entre a diferença dos valores pelo valor real,
    em modulo'''


    erro_relativo = (valor_real - valor_aproximado) / valor_real


    if erro_relativo < 0:
        return round(-erro_relativo,7)
    else:
        return round(erro_relativo,7) 
    

# Teste da função erro relativo 

def test_erro_relativo():
    assert erro_relativo(3.141592, 3.14) == 0.0005067
    assert erro_relativo(2.718282, 2.72) == 0.000632
    assert erro_relativo(1.414214, 1.41 ) == 0.0029797
    

