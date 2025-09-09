def merge_sort(lst):
    #Base case: list with 0 or 1 element is already sorted
    if len(lst) <= 1:
        return lst
    #divide 
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    #merge
    return merge(left_sorted, right_sorted)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

lst = eval(input('Enter the list:  '))
print(merge_sort(lst))
