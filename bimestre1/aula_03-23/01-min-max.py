def getMin(list):
    min = list[0]
    for i in list:
        if i < int(min):
            min = i
    return min

def getMax(list):
    max = list[0]
    for i in list:
        if i > int(max):
            max = i
    return max

list = [12, 23, 1, 34, 45, 56, 67, 89, 78]

print(f"list: {list}")
print(f"min: {getMin(list)}, max: {getMax(list)}")