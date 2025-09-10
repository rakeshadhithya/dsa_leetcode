#LINK: https://www.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1

def distribute(lst, m):
    if m > len(lst):
        return None
    #sort
    lst.sort()
    #initial window
    min_dif = lst[m-1] - lst[0]
    #slide, dont add/sub to window, find curr value update min that's it
    for right in range(m, len(lst)):
        cur_dif = lst[right] - lst[right - m + 1]
        min_dif = min(min_dif, cur_dif)
    return min_dif
lst = eval(input('Enter the list:  '))
m = int(input('Enter m:  '))
print(distribute(lst, m))

#TC: O(NlogN) : sort method O(NlogN) + right takes O(N)
#SC: O(1) : all stroes constant space O(1)