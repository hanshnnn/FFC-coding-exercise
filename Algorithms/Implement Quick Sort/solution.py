def partition(array, start, end):
    if start == end:
        return -1
    else:
        i = start - 1
        pivot = array[end]
        for j in range(start, end):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i+1], array[end] = array[end], array[i+1]
        if i == -1:
            i = 0
        return i


def quick_sort(array, start, end):
    p_index = partition(array, start, end)
    if p_index != -1:
        array = quick_sort(array, 0, p_index)
        array = quick_sort(array, p_index + 1, end)
    return array


print(quick_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92], 0, 16))  # yessss T.T
