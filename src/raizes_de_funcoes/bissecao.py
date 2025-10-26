def bissecao(f, a, b, tol=1e-6, max_iter=100):
    """
    Encontra uma raiz de f(x) = 0 no intervalo [a, b] usando o método da bisseção.
    
    Args:
        f (callable): Função contínua definida como f(x).
        a (float): Limite inferior do intervalo.
        b (float): Limite superior do intervalo.
        tol (float, opcional): Tolerância para o erro. Padrão é 1e-6.
        max_iter (int, opcional): Número máximo de iterações. Padrão é 100.

    Returns:
        float: Aproximação da raiz de f(x) = 0.

    Raises:
        TypeError: Se o parâmetro f não for uma função.
        TypeError: Se o número de iterações não for inteiro.
        ValueError: Se a tolerância não for positiva.
        ValueError: Se o número de iterações não for positiva.
        ValueError: Se f(a) e f(b) não tiverem sinais opostos.
        RuntimeError: Se o número máximo de iterações for atingido sem convergência.
    """
    if not callable(f):
        raise TypeError("O parâmetro f deve ser uma função.")
    if not int(max_iter):
        raise TypeError("O número máximo de iterações deve ser inteiro.")
    if tol <= 0:
        raise ValueError("A tolerância deve ser positiva.")
    if max_iter <= 0:
        raise ValueError("O número máximo de iterações deve ser positivo.")
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) e f(b) devem ter sinais opostos.")
    
    for _ in range(max_iter):
        x_m = (a + b) / 2
        f_m = f(x_m)
        
        if abs(f_m) < tol or (b - a) / 2 < tol:
            return x_m
        
        if f(a) * f_m < 0:
            b = x_m
        else:
            a = x_m
    
    raise RuntimeError("Número máximo de iterações atingido sem convergência.")


if __name__ == "__main__":
    f = lambda x: x**2 - 2
    raiz = bissecao(f, 1, 2)
    print(raiz)
