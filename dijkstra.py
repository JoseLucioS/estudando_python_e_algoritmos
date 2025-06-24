grafo = {}
grafo["inicio"] = {}
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2
grafo["a"] = {}
grafo["a"]["fim"] = 1
grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5
grafo["fim"] = {}

infinito = float("inf")

custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

processados = []

def ache_nodo_custo_menor(custos):
    custo_menor = float("inf")
    nodo_custo_menor = None
    for nodo in custos:
        custo = custos[nodo]
        if custo < custo_menor and nodo not in processados:
            custo_menor = custo
            nodo_custo_menor = nodo
    return nodo_custo_menor

def dijkstra(grafo, custos, pais):
    nodo = ache_nodo_custo_menor(custos)
    while nodo is not None:
        custo = custos[nodo]
        vizinhos = grafo[nodo]
        for vizinho in vizinhos.keys():
            novo_custo = custo + vizinhos[vizinho]
            if custos[vizinho] > novo_custo:
                custos[vizinho] = novo_custo
                pais[vizinho] = nodo
        processados.append(nodo)
        nodo = ache_nodo_custo_menor(custos)

if __name__ == "__main__":
    print("Custo inicial:", custos)
    print("Pais iniciais:", pais)
    print("Processados iniciais:", processados)
    print("Grafo:", grafo)
    print("\nIniciando o algoritmo de Dijkstra...\n")
    print("Nodos com custo menor:", end=' ')
    print(ache_nodo_custo_menor(custos))
    print("Processados:", processados)
    print("Custos:", custos)
    print("Pais:", pais)
    print("\nResultado final:\n")
    print("Custos:", custos)
    print("Pais:", pais)
    print("Processados:", processados)