#LINK: https://www.geeksforgeeks.org/dsa/prefix-sum-array-implementation-applications-competitive-programming/

#FOR PROBLEMS THAT ARE INCLUSIVE OF CURRENT INDEX
arr = eval(input('Enter the array:  '))
prefix_arr = [0] * len(arr)
prefix_arr[0] = arr[0]
for i in range(1, len(arr)):
    prefix_arr[i] = prefix_arr[i-1] + arr[i]
print(prefix_arr)

#TC: O(N) : prefix_array creation O(N) + i iterates through each element from 2nd to end O(N)
#SC: O(N) : prefix_array O(N)