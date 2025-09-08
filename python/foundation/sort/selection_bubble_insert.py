#sample input: [9, 5, 1, 4, 3, -1, -34]

#SELECTION SORT: for each number, find index of smallest no. RIGHT of it which is less than number. swap two.
lst = eval(input('Enter the list:  '))
for i in range(len(lst) - 1):
    min_index = i
    for j in range(i+1, len(lst)):
        if lst[j] < lst[min_index]:
            min_index = j
    lst[i], lst[min_index] = lst[min_index], lst[i]
print(f'SELECTION SORT: {lst}')

#BUBBLE SORT: for len(lst) iterations, from 0 to len(lst) - nth iteration, if curr element < next element, swap them.
lst = eval(input('Enter the list:  '))
for i in range(len(lst)):
    for j in range(len(lst) - 1 - i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(f'BUBBLE SORT: {lst}')

#INSERTION SORT: from 1st to last element, move all elements to the left of it by 1 pos which are > element else stop
# and insert there
lst = eval(input('Enter the list:  '))
for i in range(1, len(lst)):
    key = lst[i]
    j = i - 1
    while j >= 0 and lst[j] > key:
        lst[j+1] = lst[j]
        j -= 1
    lst[j+1] = key
print(f'INSERTION SORT:  {lst}')

#TC: O(N^2) for all three
#SC: O(1) because we are sorting in place


