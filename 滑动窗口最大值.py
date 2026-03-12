from ast import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        q = deque()
        for i,x in enumerate(nums):
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(i)
            left = i - k + 1
            if q[0] < left:
                q.popleft()
            if left >= 0:
                ans.append(nums[q[0]])
        return ans