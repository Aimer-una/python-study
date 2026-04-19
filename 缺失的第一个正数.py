from ast import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        n = len(nums)
        if 1 not in nums:
            return 1

        for i in range(n):
            if nums[i] <=0 or nums[i] > n:
                nums[i] = 1

        for i in range(n):
            num = abs(nums[i]) - 1
            nums[num] = -abs(nums[num])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n+1
