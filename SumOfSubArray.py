def SumOfSubArray(array):
    prefixArray = []
    prefixSum = 0

    for i in range(len(array)):
        prefixSum += array[i]
        prefixArray.append(prefixSum)

    result = 0

    for i in range(len(array)):
        for j in range(i, len(array)):
            if i == 0:
                result += prefixArray[j]
            else:
                result += prefixArray[j] - prefixArray[i - 1]

    return result
array=list(map(int,input().split()))
print(SumOfSubArray(array))