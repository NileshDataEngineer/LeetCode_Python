from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        lst = m + n - 1
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[lst] = nums1[m - 1]
                m -= 1
            else:
                nums1[lst] = nums2[n - 1]
                n -= 1
            lst -= 1
        while n > 0:
            nums1[lst] = nums2[n - 1]
            n, lst = n - 1, lst - 1
        print(nums1)
        print("Python")
        """
        Do not return anything, modify nums1 in-place instead.
        """
