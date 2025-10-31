from .minimos_quadrados.minimos_quadrados import minimos_quadrados
from .theil_sen.theil_sen import theil_sen
from .ajuste_polinomial_min_quadrados.ajuste_polinomial_min_quadrados import ajuste_polinomial_min_quadrados
from .plotagem.plot_linear_minimos_quadrados import plot_linear_minimos_quadrados
from .plotagem.plot_linear_theil_sen import plot_linear_theil_sen

__all__ = [
    'minimos_quadrados',
    'theil_sen',
    'ajuste_polinomial_min_quadrados',
    'plot_linear_minimos_quadrados',
    'plot_linear_theil_sen',
]
