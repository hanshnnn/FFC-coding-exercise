def pairwise(arr, arg):
    _sum = 0
    for i in range(len(arr)):
        for j in range(i+1, len((arr))):
            if arr[i] != 'x' and arr[j] != 'x' and arr[i] + arr[j] == arg:
                _sum = _sum + i + j
                arr[i] = 'x'
                arr[j] = 'x'
                break
    return _sum


print(pairwise([1, 4, 2, 3, 0, 5], 7))  # input goes here
