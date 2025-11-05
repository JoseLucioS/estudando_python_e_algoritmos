#Solução menos performática para encontrar o índice pivô em uma lista de números.
def findPivotIndex(nums):
    sumLeft = [0]*len(nums)
    sumRight = [0]*len(nums)
    
    #fill the sumLeft
    running = 0
    for i in range(len(nums)):
        sumLeft[i] = running
        running += nums[i]
    #fill the sumRight
    running = 0
    for i in range (len(nums)-1, -1, -1):
        sumRight[i] = running
        running += nums[i]
    
    for i in range (len(nums)):
        if sumLeft[i] == sumRight[i]:
            return i
    return -1

#solução otimizada.
def pivotIndex(nums):
    total = sum(nums)
    left = 0

    for i in range(len(nums)):
        if left == total - left - nums[i]:
            return i
        left += nums[i]
    
    return -1

if __name__ == "__main__":
    nums = [1, 7, 3, 6, 5, 6]
    nums2 = [1, 2, 3]
    nums3 = [2, 1, -1]

    print(findPivotIndex(nums))
    print(findPivotIndex(nums2))
    print(findPivotIndex(nums3))

    print(pivotIndex(nums))
    print(pivotIndex(nums2))
    print(pivotIndex(nums3))