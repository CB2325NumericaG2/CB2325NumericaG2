class Interpolacao:
    '''1a versão da interpolação linear (apenas para R²).
        No caso do R², você pode tanto dar um valor intermediário entre x0 e x1 (retorna y)
        quanto um t entre 0 e 1 (retorna [x, y]).
    '''
    @staticmethod
    def linear(a, b, x = None, t = None):
        vetor = []
        if len(a) != len(b):
            raise ValueError(f"Os pontos devem ser de mesma dimensão")
        if x is None and t is None:
            raise ValueError('Algum dos parâmetros devem ser passados')
        if x is not None and t is not None:
            raise ValueError('Apenas um dos valores devem ser passados')
        if x is not None:
            if len(a) != 2 and len(b) != 2:
                raise ValueError('Parâmetro x deve ser dado apenas para vetores no R2')
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


interp = Interpolacao()
print(interp.linear([2, 4], [6, 12], t = 1/4))
print(interp.linear([2, 4, 6], [6, 7, 4], t = 1/4))