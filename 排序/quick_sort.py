sort = [1,5,6,3,8,9]

def quick_sort(sort):
    if len(sort) < 2:
        return sort
    else:
        p = sort[0]
        biger_than_p = [i for i in sort if i > p]
        smoller_than_p = [i for i in sort if i < p]
        return quick_sort(biger_than_p) + [p] + quick_sort(smoller_than_p)

print(quick_sort(sort))