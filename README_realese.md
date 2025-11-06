# Referências

- [Referências](#referências)
  - [Erros Numéricos](#erros-numéricos)
  - [Raízes de funções](#raízes-de-funções)
  - [Interpolações](#interpolações)
    - [`linear`](#linear)
  - [Funções Aproximadoras](#funções-aproximadoras)
  - [Integrações Numéricas](#integrações-numéricas)
    - [Usando `integracao_trapezio`](#usando-integracao_trapezio)

## Erros Numéricos

| Métodos                                                   | Descrição                                           | Argumentos                                              |
|-----------------------------------------------------------|-----------------------------------------------------|---------------------------------------------------------|
| `erro_absluto`                            | Calcula o erro absoluto de dois valores             |                                                         |
| `erro_relativo`                   | Calcula o errro relativo de um intervalo            |                                                         |                                                         |

## Raízes de funções

| Métodos                                   | Descrição                                           | Argumentos                                              |
|-------------------------------------------|-----------------------------------------------------|---------------------------------------------------------|
| `newton_raphson`                          | Calcula o erro absoluto de dois valores             |                                                         |
| `biseccao`                                | Calcula o errro relativo de um intervalo            |                                                         |                                                         |
| `secante`                                 | Calcula o errro relativo de um intervalo            |                                                         |                                                         |

Você pode ver

## Interpolações

| Métodos                                   | Descrição                                           | Argumentos                                              |
|-------------------------------------------|-----------------------------------------------------|---------------------------------------------------------|
| `linear`                  | Calcula o erro absoluto de dois valores             |                                                         |
| `linear_partes`           | Calcula o errro relativo de um intervalo            |                                                         |                                                         |

### `linear` 



## Funções Aproximadoras
| Métodos                                   | Descrição                                           | Argumentos                                              |
|-------------------------------------------|-----------------------------------------------------|---------------------------------------------------------|
| `theil_sen`                         | Calcula o erro absoluto de dois valores             |                                                         |
| `minimos_quadrados`           | Calcula o errro relativo de um intervalo            |                                                         |                                                         |
| `regressao_linear`           | Calcula o errro relativo de um intervalo            |                                                         |                                                         |

## Integrações Numéricas

| Métodos                                   | Descrição                                           | Argumentos                                              |
|-------------------------------------------|-----------------------------------------------------|---------------------------------------------------------|
| `integracao_trapezio`            | Calcula o erro absoluto de dois valores             |                                                         |
| `integracao_retangulo`           | Calcula o errro relativo de um intervalo            |                                                         |                                                         |
| `integracao_componentes`           | Calcula o errro relativo de um intervalo            |                                                         |                                                         |

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