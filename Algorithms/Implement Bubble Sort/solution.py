def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                array[j+1], array[j] = array[j], array[j+1]
    return array


print(bubble_sort([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]))  #viola
