def soma_recursiva(array):
    if not array:
        return 0
    else:
        return array[0] + soma_recursiva(array[1:])

def soma_recursiva_v2(array):
    if not array:
        return 0
    else:
        return array.pop(0) + soma_recursiva(array)


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6]
    print(soma_recursiva(array))
    print(soma_recursiva_v2(array))