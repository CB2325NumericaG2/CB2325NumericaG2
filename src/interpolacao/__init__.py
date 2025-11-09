from .linear import interpolacao_linear as linear
from .linear_partes import interpolacao_linear_partes as linear_partes
from .interpolacao_polinomial import PolinomioInterpolador as polinomial

__all__ = ["linear_partes", "linear", "polinomial"]
