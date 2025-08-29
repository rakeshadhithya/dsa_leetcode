#LINK: https://www.hackerearth.com/problem/algorithm/palindrome-check-2-1/
from collections import Counter
name = input()                  
freq = Counter(name)
odd_count = sum( 1 for f in freq.values() if f % 2 != 0)
print('YES') if odd_count < 2 else print('NO')

#TC: O(N) : Counter function traverses each char to count its freq O(N) + f in sum() 
# iterates through each value O(1) due to limited chars
#SC: O(1) : Counter function stores count of limited chars(max 512). 
# note alphabet size is denoted by Lowercase sigma (σ) instead of O(1), write O(σ) to be precise

