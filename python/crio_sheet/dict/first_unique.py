#Later

from collections import deque, Counter

class FirstUnique:
    def __init__(self, nums):
        self.count = Counter(nums)
        self.queue = deque([num for num in nums if self.count[num] == 1])

    def showFirstUnique(self):
        while self.queue and self.count[self.queue[0]] > 1:
            self.queue.popleft()
        return self.queue[0] if self.queue else -1

    def add(self, value):
        self.count[value] += 1
        if self.count[value] == 1:
            self.queue.append(value)


#TC: 3 phases: for initialisation O(N), show first unique O(1) amortised, add(value) O(1)
#SC: for count O(N+M), for queue O(N+M) for M elements added after initialisation