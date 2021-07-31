def swab(string, i, length):
    string = list(string)
    global combinations
    if i == length:
        combinations.append(string)
    else:
        for j in range(i, length):
            string[i], string[j] = string[j], string[i]
            swab(string, i + 1, length)
            string[i], string[j] = string[j], string[i]


def perm_alone(combinations):
    no_repeat = 1
    count = 0
    for combination in combinations:
        for i in range(len(combination)-1):
            if combination[i] == combination[i+1]:
                no_repeat = 0
                break
        if no_repeat:
            count += 1
        no_repeat = 1
    return count


combinations = []
test = "aaabb" # input goes here
swab(test, 0, len(test))
print(perm_alone(combinations))
