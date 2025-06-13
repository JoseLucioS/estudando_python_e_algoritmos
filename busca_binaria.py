#Busca Binaria em um lista ordenada
def busca_binaria_ordenada(lista, item):
    inicio = 0
    fim = len(lista) - 1
 
    while inicio <= fim:
        meio = (inicio+fim) // 2
        palpite = lista[meio]
        if palpite == item:
            return meio
        if palpite < item:
            inicio = meio + 1
        else:
            fim = meio - 1
    return None

#Busca Binaria em um lista desordenada, uma vez que ordena a lista antes de realizar a busca
def busca_binaria_desordenada(lista, item):
    lista = sorted(lista)
    
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio+fim) // 2
        palpite = lista[meio]
        if palpite == item:
            return meio
        if palpite < item:
            inicio = meio + 1
        else:
            fim = meio - 1
    return None


if __name__ == "__main__":
    lista_ordenada = [1, 2, 3, 12, 14, 16, 20, 45, 89, 100]
    lista_desordenada = [1, 3, 6, 4, 76, 45, 21, 32, 100, 90]

    print(busca_binaria_ordenada(lista_ordenada, 20)) #espera 6 como resultado
    print(busca_binaria_desordenada(lista_desordenada, 100)) #espera 9 como resultado
    print(busca_binaria_desordenada(lista_desordenada, -1)) #espera None como resultado