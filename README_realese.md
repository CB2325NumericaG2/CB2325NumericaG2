# Referências

- [Referências](#referências)
  - [Erros Numéricos](#erros-numéricos)
  - [Raízes de funções](#raízes-de-funções)
  - [Interpolações](#interpolações)
  - [Funções Aproximadoras](#funções-aproximadoras)
  - [Integrações Numéricas](#integrações-numéricas)
    - [Usando `integracao_trapezio`](#usando-integracao_trapezio)

## Erros Numéricos

| Métodos                                                   | Descrição                                                                   | Argumentos                                                                                                                                             |
|-----------------------------------------------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| `erro_absluto`                                            | Calcula o erro absoluto de dois valores                                     | `valor_real`: valor real <br> `valor_aproximado`: valor aproximado                                                                                     |
| `erro_relativo`                                           | Calcula o errro relativo de um intervalo                                    | `valor1`: primeiro valor <br> `valor2`: segundo valor                                                                                                  |

## Raízes de funções

| Métodos                                                   | Descrição                                                                   | Argumentos                                                                                                                                             |
|-----------------------------------------------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| `newton_raphson`                                          | Calcula o erro absoluto de dois valores                                     | `f`: função f(x) <br> `x0`: ponto inicial <br> `tol`: tolerância <br> `max_iter`: número máximo de iterações<br> `df`: Derivada de f(x)                |
| `biseccao`                                                | Calcula o errro relativo de um intervalo                                    | `f`: função f(x) <br> `a`: menor do intervalo <br> `b`: maior do intervalo <br> `tol`: tolerancia <br> `max_iter`: número de iterações máxima          |
| `secante`                                                 | Calcula o errro relativo de um intervalo                                    |

Você pode ver

## Interpolações

| Métodos                                                   | Descrição                                                                   | Argumentos                                                                                                                                             |
|-----------------------------------------------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| `linear`                                                  | Faz a interpolação linear de uma escala e obtém o valor correspondente.     | `a`: primeiro ponto <br> `b`: segundo ponto <br> `x`: valor independente entre `a` e `b` <br> `t`: parâmetro da interpolação entre 0 e 1               |                                        |
| `linear_partes`                                           | Faz a interpolação po partes de acordo com o número de amostras.            |                                                                                                                                                        |

<!-- ### `linear`  -->

## Funções Aproximadoras
| Métodos                                                   | Descrição                                                                   | Argumentos                                                                                                                                             |
|-----------------------------------------------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| `theil_sen`                                               | Calcula o erro absoluto de dois valores                                     |                                                                                                                                                        |
| `minimos_quadrados`                                       | Calcula o errro relativo de um intervalo                                    |                                                                                                                                                        |
| `regressao_linear`                                        | Calcula o errro relativo de um intervalo                                    |                                                                                                                                                        |

## Integrações Numéricas

| Métodos                                                   | Descrição                                                                   | Argumentos                                                                                                                                            |
|-----------------------------------------------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| `integral_trapezio`                                       | Calcula o erro absoluto de dois valores                                     |                                                                                                                                                       |
| `integral_retangulo`                                      | Calcula o errro relativo de um intervalo                                    |                                                                                                                                                       |
| `integral_componentes`                                    | Calcula o errro relativo de um intervalo                                    |                                                                                                                                                       |

### Usando `integracao_trapezio`

> __ATENÇÃO__: A integração por `integracao_trapezio` ela não é exata

```python
from CB2325NumericaG2 import integracao_trapezio, erro_absoluto

import math

from sympy import integrate, symbols

f = lambda x: math.sin(x**2)
INTERVALS = 100


exact_f_val = integrate(f, a, b)
appr_f_val = integracao_trapezio(f, a, b, INTERVALS)

err = erro_absoluto(exact_f_val - appr_f_val)

print(f"Aproximação da função sin(x^2) com {INTERVALS} foi de: {err}")


```