def merge_sort(array, start, end):
    if end - start == 2:
        if array[start] > array[start + 1]:
            array[start + 1], array[start] = array[start], array[start + 1]
    # when a pair contains only one block
    elif end - start == 1:
        pass
    else:
        pivot = start + (end - start) // 2
        merge_sort(array, start, pivot)
        merge_sort(array, pivot, end)
        count = end - start
        l, r = start, pivot
        temp = [0 for x in range(count)]
        # main merging work
        for x in range(len(temp)):
            if r == end or (array[l] < array[r] and l < pivot):
                temp[x] = array[l]
                l += 1
            else:
                temp[x] = array[r]
                r += 1
        array[start:end] = temp
    return array


print(merge_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92], 0, 17))
