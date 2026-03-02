from ast import List


def swap(nums, left, right):
    temp = nums[left]
    nums[left] = nums[right]
    nums[right] = temp


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        right = 0
        left = 0
        while right < n:
            if nums[right] != 0:
                swap(nums, left, right)
                left += 1
            right += 1
