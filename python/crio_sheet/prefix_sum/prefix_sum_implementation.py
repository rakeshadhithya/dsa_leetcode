#LINK: https://www.geeksforgeeks.org/dsa/prefix-sum-array-implementation-applications-competitive-programming/

arr = eval(input('Enter the array:  '))
prefix_arr = [0] * len(arr)
prefix_arr[0] = arr[0]
for i in range(1, len(arr)):
    prefix_arr[i] = prefix_arr[i-1] + arr[i]
print(prefix_arr)