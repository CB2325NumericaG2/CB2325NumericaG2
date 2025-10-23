
#discutir com Gabi Ogido sobre os tipos de interpolação serem classes ou subclasses

class InterpolacaoLinear:
    '''1a versão da interpolação linear (apenas para R²).
        No caso do R², você pode tanto dar um valor intermediário entre x0 e x1 (retorna y)
        quanto um t entre 0 e 1 (retorna [x, y]).
    '''
    def __init__(self, a, b):
        self.a = a
        self.b = b
        if len(self.a) != len(self.b):
            raise ValueError(f"Os pontos devem ser de mesma dimensão")
    
    def __call__(self, x):
        x_min, x_max = sorted([self.a[0], self.b[0]])
        if not x_min <= x <= x_max:
            raise ValueError(f"x={x} está fora do intervalo [{x_min}, {x_max}].")
        return self.a[1] + (self.b[1] - self.a[1])/(self.b[0] - self.a[0]) * (x - self.a[0])
    
    def interp_parametric(self, t):
        if not 0 <= t <= 1:
            raise ValueError('t deve estar entre 0 e 1.') 
        return [(1-t) * self.a[0] + t * self.b[0], (1-t) * self.a[1] + t * self.b[1]]
            
    
interp = InterpolacaoLinear([2, 4], [6,12])
print(interp(3)) # retorna 6.0
print(interp.interp_parametric(1/4)) # retorna [3.0, 6.0]
print(interp(7)) # retorna ValueError (fora do intervalo) 
print(interp.interp_parametric(2)) # retorna ValueError (t fora de [0,1])
interp2 = InterpolacaoLinear([2,4], [6, 12, 4])
print(interp2(7)) # retorna ValueError (dimensões diferentes)
print(interp2.interp_parametric(1/4)) # retorna ValueError (dimensões diferentes)