class Solution:
    def solve(self, nums):
        u_nums = []
        for i in range(0,len(nums)):
            if nums[i] not in u_nums:
                u_nums.append(nums[i])
        return len(u_nums)