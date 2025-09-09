def quick_sort(lst):
    #Base case: list with 0 or 1 element is already sorted
    if len(lst) <= 1:
        return lst
    #take middle as pivot
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

lst = eval(input('Enter the list:  '))
print(quick_sort(lst))