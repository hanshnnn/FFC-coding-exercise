def selection_sort(array):
    for i in range(len(array)-1):
        small = max(array)
        small_index = -1
        for j in range(i, len(array)):
            if array[j] < small:
                small, small_index = array[j], j
        if small_index != -1:
            array[i], array[small_index] = array[small_index], array[i]
    return array


print(selection_sort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]))  #viola
