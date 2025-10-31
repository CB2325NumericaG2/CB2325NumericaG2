import numpy as np

def ajuste_polinomial_min_quadrados(x: list[float], y: list[float], grau: int, cond_thresh=1e12):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    # Vamos criar uma matriz (n x m)
    # n Ǹ o grau do polin��mio 
    # m Ǹ o nǧmero de coordenadas que o usuǭrio utilizar

    m = len(x)
    
    if m != len(y): 
        # O usuǭrio errou ao enviar dados para a fun��ǜo.
        raise ValueError(f"len(x)={m} diferente de len(y)={len(y)}")
    
    # Teste direto de reta vertical
    if np.allclose(x, x[0]):
        # Todos os valores de x sǜo iguais ��' reta vertical
        return np.array([x[0], True], dtype=object)
    
    # Reduz o grau se houver menos pontos que coeficientes
    if m < grau + 1:
        return ajuste_polinomial_min_quadrados(x, y, m - 1, cond_thresh)
    
    # Matriz de Vandermonde
    X = np.vander(x, grau + 1, increasing=True)
    
    # Nǧmero mǭximo de colunas linearmente independentes (rank)
    sigma = np.linalg.svd(X, compute_uv=False)
    # Tolerǽncia baseada no condicionamento numǸrico
    _tol = sigma[0] / cond_thresh
    rank = np.linalg.matrix_rank(X, tol=_tol)
    
    # Ajusta o grau com base no posto da matriz
    if rank < X.shape[1]:
        X = np.vander(x, rank, increasing=True)
    
    # Lista dos coeficientes do polin��mio via m��nimos quadrados diretos
    a = np.linalg.inv(X.T @ X) @ X.T @ y

    # O ǧltimo valor do array indica se a fun��ǜo Ǹ uma reta vertical
    a = np.append(a, False)

    return a

