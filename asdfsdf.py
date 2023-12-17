def getResult(n,arr):
    result =[]

    arr.sort()
    arr = set(arr)
    result.append(arr[-2])
    result.append(arr[1])
    return result



