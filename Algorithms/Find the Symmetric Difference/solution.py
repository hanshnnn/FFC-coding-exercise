def sym(*args):
    i, j = 0, 1
    result = args[i]
    while j < len(args):
        temp = []
        common = [element for element in args[j] if element in result]
        for element in args[j]:
            if element not in common:
                result.append(element)
        for element in result:
            if element not in common and element not in temp:
                temp.append(element)
        result = temp
        j += 1
        i += 1
    result.sort()
    return result


print(sym([1, 2, 3], [5, 2, 1, 4]))
print(sym([1, 2, 3, 3], [5, 2, 1, 4]))
print(sym([1, 2, 3], [5, 2, 1, 4, 5]))
print(sym([1, 2, 5], [2, 3, 5], [3, 4, 5]))
print(sym([1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5]))
print(sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3]))
print(sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1]))
© 2021 GitHub, Inc.
