#LINK: https://leetcode.com/problems/removing-minimum-and-maximum-from-array/


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        #initialise ptrs and values(take less and more than constraint values)
        min_index = max_index = 0
        minimum = float('inf')
        maximum = - float('inf')
        #find minmum's index, maximum's index
        for index in range(len(nums)):
            if nums[index] > maximum:
                maximum = nums[index]
                max_index = index
            if nums[index] < minimum:
                minimum = nums[index]
                min_index = index
        #find which is to the left, right then calculate min part size to remove both left and right indices(from start to right, from start to left and right to end, from end to left)
        left = min(min_index, max_index)
        right = max(min_index, max_index)
        return min( right + 1, left + 1 + len(nums) - right, len(nums) - left )
        