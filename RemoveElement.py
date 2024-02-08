from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[l] = nums[i]
                l += 1
        return l

nums = [0,1,2,2,3,0,4,2]
val = 2

leetcode = Solution()
result = leetcode.removeElement(nums,val)
print(result)