def newton_raphson(f, x0, tol=1e-6, max_iter=100, df=None):
    """
    Método de Newton-Raphson para encontrar uma raiz de f(x)=0.

    Args:
        f (callable): função (definida como f(x)).
        x0 (float): aproximação inicial.
        tol (float, opcional): tolerância para o erro (critério de parada).
        max_iter (int, opcional): número máximo de iterações.
        df (callable, opcional): derivada de f(x); se None, será calculada numericamente.

    Returns: 
        float: Aproximação da raiz de f(x) = 0.
    
    Raises:
        TypeError: Se o parâmetro f não for uma função.
        TypeError: Se o número de iterações não for inteiro.
        ValueError: Se a tolerância não for positiva.
        ValueError: Se o número de iterações não for positiva.
        ZeroDivisionError: Se a derivada for nula em algum ponto utilizado.
        RuntimeError: Se o número máximo de iterações for atingido sem convergência.
    """
    if not callable(f):
        raise TypeError("O parâmetro f deve ser uma função.")
    if not int(max_iter):
        raise TypeError("O número máximo de iterações deve ser inteiro")
    if tol <= 0:
        raise ValueError("A tolerância deve ser positiva.")
    if max_iter <= 0:
        raise ValueError("O número máximo de iterações deve ser positivo.")

    # Derivada numérica (se não fornecida)
    if df is None:
        def df(x, h=1e-6):
            return (f(x + h) - f(x - h)) / (2 * h)

    for i in range(max_iter):
        f_x = f(x0)
        df_x = df(x0)

        if df_x == 0:
            raise ZeroDivisionError("Derivada nula — método falha em x = {:.6f}".format(x0))

        x1 = x0 - f_x / df_x

        if abs(x1 - x0) < tol:
            return x1

        x0 = x1

    raise RuntimeError("Número máximo de iterações atingido sem convergência.")


if __name__ == "__main__":
    f = lambda x: x**2 - 2
    df = lambda x: 2*x
    raiz = newton_raphson(f, 1, df = df)
    print(raiz)