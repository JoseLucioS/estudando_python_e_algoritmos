from collections import deque

def pessoa_e_vendedor(nome):
    return nome[-1] == 'm'

#implementação da busca em largura
def pesquisa(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    verificados = []

    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificados:
            if pessoa_e_vendedor(pessoa):
                print(pessoa + " é um vendedor de kimonos!")
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificados.append(pessoa)

    return False


grafo = {}
grafo["voce"] = ["alice", "bob", "claire"]
grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []


#print(fila_de_pesquisa)
print(pesquisa("voce"))

