# -*- coding: utf-8 -*-

def selection_sort(list):
    length = len(list)
    for i in range(length - 1, 0, -1):
        for j in range(i):
            if list[j] > list[i]:
                list[j], list[i] = list[i], list[j]
    return list

test_list = [3,5,2,7,5,9,1]


print(selection_sort(test_list))
