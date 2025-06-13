#Encontra o menor elemento de uma lista
def encontrar_menor(lista):
    menor = lista[0]
    menor_index = 0
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            menor_index = i
    
    return menor_index

#Ordena uma lista por seleção, do menor para o maior elemento
def selection_sort(lista):
    lista_ordenada = []

    for i in range(len(lista)):
        menor = encontrar_menor(lista)
        lista_ordenada.append(lista.pop(menor))

    return lista_ordenada

if __name__ == "__main__":
    # Exemplo de uso
    lista = [5, 2, 3, 1, 9, 12, 54, 34, 78, 65]
    print("Lista original:", lista)
    
    lista_ordenada = selection_sort(lista)
    print("Lista ordenada:", lista_ordenada)