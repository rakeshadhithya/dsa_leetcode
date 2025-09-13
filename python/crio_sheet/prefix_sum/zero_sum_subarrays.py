#LINK: https://www.geeksforgeeks.org/problems/zero-sum-subarrays1825/1

arr = eval(input('Enter the array:  '))

prefix_sum = 0
count = 0
prefixsum_count = {}
for num in arr:
    prefix_sum += num
    if prefix_sum == 0:
        count += 1
    if prefix_sum in prefixsum_count:
        count += prefixsum_count[prefix_sum]
    prefixsum_count[prefix_sum] = prefixsum_count.get(prefix_sum, 0) + 1
print(f'No. of subarrays that have zero sum is : {count}')

#TC: O(N) : num iterates through each number in nums O(N)
#SC: O(N) prefixsum_count stores O(N) in worst case