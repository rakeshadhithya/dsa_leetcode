#Find the length of longest substring with at most k distinct characters

def find_longest(string, k):
    if k > len(string):
        return k
    #initial window
    left = 0
    dct = {}
    max_len = -float('inf')
    for right in range(len(string)):
        #increment count of right
        dct[string[right]] = dct.get(string[right], 0) + 1
        #if total chars in dct exceed k, remove from left
        if len(dct) > k:
            dct[string[left]] -= 1
            if dct[string[left]] == 0:
                del dct[string[left]]
            left += 1
        #update max
        max_len = max(max_len, right - left + 1)
    return max_len

string = input('Enter any string:  ')
k = int(input('Enter max number of distinct chars:  '))
print(find_longest(string, k))

'''
test cases:
print(find_longest("eceba", 2))       # Expected: 3 → "ece"
print(find_longest("aaabc", 2))       # Expected: 4 → "aaab"
print(find_longest("abcabcbb", 3))    # Expected: 8 → "abcabcbb"

'''