class Solution:
    def solve(self, nums):
        count = 1
        for i in range(0,len(nums)-1):
            if (nums[i] != nums[i+1]):
                count += 1
        return count