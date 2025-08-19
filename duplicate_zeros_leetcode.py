#questao 1089 do leetcode

def duplicateZeros(arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = arr.count(0)
        arr_length = len(arr)

        for i in range(arr_length-1, -1, -1):
            if i + zeros < arr_length:
                arr[i+zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < arr_length:
                    arr[i+zeros] = 0


if __name__ == "__main__":
    array = [1,0,2,3,0,4,5,0]
    duplicateZeros(array)
    print(array)