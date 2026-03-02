class Solution:
    def twoSum(self, nums, target):
        map1 = {}

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i,num in enumerate(nums):
            if target - num in map1:
                return map1[target - num],i
            map1[num] = i
        return [-1,-1]