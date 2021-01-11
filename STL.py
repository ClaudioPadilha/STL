import numpy as np

def numero_ilhas(mapa):
    """ Devolve o numero de ilhas no mapa (considere vizinança 4-conexa)
    Algoritmo baseado no Quick-Union, seção 1.5 do livro "Algorithms" R. Saedgewick, K. Wayne """
    
    mapa = np.array(mapa, dtype=np.int)
    
    N, M = mapa.shape
    
    # aplicar zero-padding preenchendo bordas com zeros
    mapa_pad = np.pad(mapa, 1, constant_values=0)
    
    # array que armazena as referencias aos nós pais
    ids = np.zeros((N * M), dtype=np.int)
    
    # cada folha é inicializada sendo seu próprio pai
    for i in range(N * M):
        ids[i] = i
    
    # subir as árvores para achar as raízes
    def raiz(i):
        while (i != ids[i]):
            i = ids[i]
        return i
    
    # percorre o mapa criando as árvores em ids
    for i in range(N):
        for j in range(M):
            k = j + M * i
            if mapa_pad[i + 1, j + 1] > 0:
                if mapa_pad[i + 2, j + 1] > 0 and (raiz(k) != raiz(k + M)):
                    ids[raiz(k + M)] = raiz(k)
                if mapa_pad[i + 1, j + 2] > 0 and (raiz(k) != raiz(k + 1)):
                    ids[raiz(k + 1)] = raiz(k)
                if mapa_pad[i, j + 1] > 0 and (raiz(k) != raiz(k - M)):
                    ids[raiz(k - M)] = raiz(k)
                if mapa_pad[i + 1, j] > 0 and (raiz(k) != raiz(k - 1)):
                    ids[raiz(k - 1)] = raiz(k)
    
    # conta o número de árvores (número de vezes em que ids[raiz] == raiz)
    n = 0
    for i in range(N):
        for j in range(M):
            k = j + M * i
            if mapa[i, j] > 0 and ids[k] == k:
                n += 1

    return n

def quantidade_de_terra_afetada(mapa, i, j):
    """Calcula o numero de pontos de solo do mapa que podem ser afetados 
    por uma semente lançada em mapa[i, j] (considere vizinhança 4-conexa)
    Algoritmo baseado no Quick-Union, seção 1.5 do livro "Algorithms" R. Saedgewick, K. Wayne """
    
    mapa = np.array(mapa, dtype=np.int)
    
    N, M = mapa.shape
    
    # aplicar zero-padding preenchendo bordas com zeros
    mapa_pad = np.pad(mapa, 1, constant_values=0)
    
    # array que armazena as referencias aos nós pais
    ids = np.zeros((N * M), dtype=np.int)
    
    # cada folha é inicializada sendo seu próprio pai
    for k in range(N * M):
        ids[k] = k
    
    # subir as árvores para achar as raízes
    def raiz(k):
        while (k != ids[k]):
            k = ids[k]
        return k
    
    # percorre o mapa criando as árvores em ids
    for p in range(N):
        for q in range(M):
            k = q + M * p
            if mapa_pad[p + 1, q + 1] > 0:
                if mapa_pad[p + 2, q + 1] > 0 and (raiz(k) != raiz(k + M)):
                    ids[raiz(k + M)] = raiz(k)
                if mapa_pad[p + 1, q + 2] > 0 and (raiz(k) != raiz(k + 1)):
                    ids[raiz(k + 1)] = raiz(k)
                if mapa_pad[p, q + 1] > 0 and (raiz(k) != raiz(k - M)):
                    ids[raiz(k - M)] = raiz(k)
                if mapa_pad[p + 1, q] > 0 and (raiz(k) != raiz(k - 1)):
                    ids[raiz(k - 1)] = raiz(k)
    
    # para pontos fora d'agua, achar todos q tem a mesma raiz que o ponto
    # onde a semente caiu (mapa[i, j] -> ids[j + i * M])
    if mapa[i, j] > 0:
        k = raiz(j + i * M)
        
        n = 0
        for p in range(N):
            for q in range(M):
                r = q + M * p
                if mapa[p, q] > 0 and raiz(r) == k:
                    n += 1
        return n
    else:
        return 0

