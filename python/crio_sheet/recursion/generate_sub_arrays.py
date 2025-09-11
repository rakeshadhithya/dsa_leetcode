def find_all_subsequences(arr, i, path, res):
    for k in range(i, len(arr)):
        path.append(arr[k])
        res.append(path.copy())
        find_all_subsequences(arr, k + 1, path, res)
        path.pop()
def find_all_subarrays(arr, start, res):
    if start == len(arr):
        return
    for end in range(start, len(arr)):
      res.append(arr[start:end+1])
    find_all_subarrays(arr, start + 1, res)

arr = eval(input('Enter the array:  '))
res = []
find_all_subarrays(arr, 0, res)
# for i in range(len(arr)):
#     for j in range(i, len(arr)):
#         res.append(arr[i:j+1])
print(res)

'''
for each index copy that index till next index
1 2 3
1 12 13  slice from i to j+1
2 23
3
for i in range(len(a)):
  for j in range(i, len(a)):
      res.append(a[i:i+1])
'''