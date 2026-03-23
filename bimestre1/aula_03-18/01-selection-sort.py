list = [64, 34, 25, 5, 22, 11, 90, 12]

def selection_sort(list):
    list_len = len(list)
    for i in range(list_len - 1):
        min_index = i
        for j in range(i + 1, list_len):
            if list[j] < list[min_index]:
                min_index = j
        min_value = list.pop(min_index)
        list.insert(i, min_value)
    return list

print(selection_sort(list))