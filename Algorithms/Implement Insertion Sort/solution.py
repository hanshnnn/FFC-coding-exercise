def insertion_sort(array):
    index = [i for i in range(len(array))]
    for i in range(1, len(array)):
        key = array[i]
        for j in range(0, i):
            if array[i] <= array[j]:
                # move every element 1 step forwards
                for k in range(i, j, -1):
                    array[k] = array[k-1]
                array[j] = key
    return array


print(insertion_sort(insertion_sort([7,6,5,4,6,2,3,1])))  #viola
