from .minimos_quadrados.minimos_quadrados import minimos_quadrados
from .theil_sen.theil_sen import theil_sen
from .ajuste_polinomial_min_quadrados.ajuste_polinomial_min_quadrados import (
    ajuste_polinomial_min_quadrados,
)
from .plotagem.plot_linear_minimos_quadrados import (
    plot_linear_minimos_quadrados,
)
from .plotagem.plot_linear_theil_sen import plot_linear_theil_sen
from .plotagem.plot_polinomio_minimos_quadrados import (
    plot_polinomio_minimos_quadrados,
)

__all__ = [
    'minimos_quadrados',
    'theil_sen',
    'ajuste_polinomial_min_quadrados',
    'plot_linear_minimos_quadrados',
    'plot_linear_theil_sen',
    'plot_polinomio_minimos_quadrados',
]

if __name__ == "__main__":
    # Demonstração simples dos métodos com dois conjuntos de dados
    X1 = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
    Y1 = [1000, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

    a, b, flag = minimos_quadrados(X1, Y1)
    if flag == 0:
        print(f"x = {b:.2f}")
    else:
        print(f"y = {a:.2f}x + {b:.2f}")
    plot_linear_minimos_quadrados(X1, Y1)

    a_ts, b_ts, flag_ts = theil_sen(X1, Y1)
    if flag_ts == 0:
        print(f"x = {a_ts:.2f}")
    else:
        print(f"y = {b_ts:.2f}x + {a_ts:.2f}")
    plot_linear_theil_sen(X1, Y1)

    # Reta vertical
    X2 = [3, 3, 3, 3]
    Y2 = [1, 2, 3, 4]

    a2, b2, flag2 = minimos_quadrados(X2, Y2)
    if flag2 == 0:
        print(f"x = {b2:.2f}")
    else:
        print(f"y = {a2:.2f}x + {b2:.2f}")
    plot_linear_minimos_quadrados(X2, Y2)

    a2_ts, b2_ts, flag2_ts = theil_sen(X2, Y2)
    if flag2_ts == 0:
        print(f"x = {a2_ts:.2f}")
    else:
        print(f"y = {b2_ts:.2f}x + {a2_ts:.2f}")
    plot_linear_theil_sen(X2, Y2)
