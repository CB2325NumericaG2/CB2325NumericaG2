def secante(f, x0, x1, tol=1e-6, max_iter=100):
    for _ in range(max_iter):
        if abs(f(x1) - f(x0)) < 1e-12:
            raise ZeroDivisionError("Diferença muito pequena")
        x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))
        if abs(x2 - x1) < tol:
            return x2
        x0, x1 = x1, x2
    raise ValueError("Número máximo de iterações atingido")

# Teste
f = lambda x: x**2 - 2
raiz = secante(f, 1, 2)
print(raiz)
