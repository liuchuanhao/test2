# -*- coding: utf-8 -*-




def bubble_sort(list):
    count = len(list)
    for i in range(count):
        for j in range(i + 1, count):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list


test_list = [3,5,2,7,5,9,1]


print(bubble_sort(test_list))
