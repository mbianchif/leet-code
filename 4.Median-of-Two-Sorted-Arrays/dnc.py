from math import inf


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n, m = len(nums1), len(nums2)
        left = (n + m + 1) // 2
        a, b = 0, n

        # O(log(n + m))
        while a <= b:
            m1 = (a + b) >> 1
            m2 = left - m1

            l1 = nums1[m1 - 1] if m1 > 0 else -inf
            r1 = nums1[m1] if m1 < n else inf
            l2 = nums2[m2 - 1] if m2 > 0 else -inf
            r2 = nums2[m2] if m2 < m else inf

            if l1 <= r2 and l2 <= r1:
                lmax = max(l1, l2)
                return lmax if (n + m) & 1 else (lmax + min(r1, r2)) / 2
            elif l1 > r2:
                b = m1 - 1
            else:
                a = m1 + 1

        return 0.0
