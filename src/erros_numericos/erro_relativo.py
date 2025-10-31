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
    


    

