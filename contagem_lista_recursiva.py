def conta_itens_lista(lista):
    if not lista:
        return 0
    else:
        return 1 + conta_itens_lista(lista[1:])
    
def conta_itens_lista_v2(lista):
    if not lista:
        return 0
    else:
        lista.pop(0)
        return 1 + conta_itens_lista(lista)
    
if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6]
    print("Número de itens na lista:", conta_itens_lista(lista))
    
    lista_vazia = []
    print("Número de itens na lista vazia:", conta_itens_lista(lista_vazia))

    print("Testando a versão v2: ", conta_itens_lista_v2(lista))