from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        mxs, dq = [], deque()

        # O(n)
        for i, x in enumerate(nums):
            if dq and dq[0] <= i - k:
                dq.popleft()

            while dq and nums[dq[-1]] < x:
                dq.pop()

            dq.append(i)
            if i >= k - 1:
                mxs.append(nums[dq[0]])

        return mxs
