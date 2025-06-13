def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        menores = [i for i in array[1:] if i <= pivo]
        maiores = [i for i in array[1:] if i > pivo]

        return quicksort(menores) + [pivo] + quicksort(maiores)

if __name__ == "__main__":
    array = [5, 2, 3, 1, 9, 12, 54, 34, 78, 65]
    print("Lista original: ", array)

    print("Lista ordenada: ", quicksort(array))