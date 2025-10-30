class Interpolacao:
    '''2a versão da interpolação linear (para Rn).
        A interpolação linear é feita com dois vetores e um parâmetro: x ou t.
        O parâmetro x é usado para vetores no R2 e corresponde à 1a componente do vetor,
        por isso deve estar entre os valores da 1a componente dos vetores passados.
        No caso em que o parâmetro x é usado, o método retorna a componente y correspondente.
        O parâmetro t é usado em qualquer dimensão  
    '''
    @staticmethod
    def linear(a, b, x = None, t = None):
        vetor = []
        if len(a) != len(b):
            raise ValueError(f"Os pontos devem ser de mesma dimensão")
        if x is None and t is None:
            raise ValueError('Algum dos parâmetros deve ser passado (x ou t).')
        if x is not None and t is not None:
            raise ValueError('Apenas um dos parâmetros deve ser passado (x ou t).')
        if x is not None:
            if len(a) != 2 or len(b) != 2:
                raise ValueError('Interpolação por x só é válida para vetores no R2')
            x_min, x_max = sorted([a[0], b[0]])
            if not x_min <= x <= x_max:
                raise ValueError(f"x={x} está fora do intervalo [{x_min}, {x_max}].")
            return a[1] + (b[1] - a[1])/(b[0] - a[0]) * (x - a[0])
        if t is not None: 
            if not 0 <= t <= 1:
                raise ValueError('t deve estar entre 0 e 1.')
            for coords1, coords2 in zip(a, b): 
                vetor.append((1-t) * coords1 + t * coords2)
            return vetor


if __name__ == "__main__":
    interp = Interpolacao()
    print(interp.linear([2, 4], [6, 12], t = 1/4))
    print(interp.linear([2, 4, 6], [6, 7, 4], t = 1/4))