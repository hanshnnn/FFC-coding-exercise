def updateInventory(old, new):
    existed = 0
    # update quantity
    for new_item in new:
        for cur_item in old:
            if new_item[1] == cur_item[1]:
                cur_item[0] += new_item[0]
                existed = 1
        if existed == 0:
            old.append(new_item)
        existed = 0
    # sorting
    names = []
    sorted_list = []
    for item in old:
        names.append(item[1])
    names.sort()
    for name in names:
        for item in old:
            if item[1] == name:
                sorted_list.append(item)
                break
    return sorted_list


curInv = [[0, "Bowling Ball"], [0, "Dirty Sock"], [0, "Hair Pin"], [0, "Microphone"]]
newInv = [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]]
print(updateInventory(curInv, newInv))
