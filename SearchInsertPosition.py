class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        for i in range(0,len(nums)):
            if nums[i] == target:
                l=i
                break
            elif nums[i] > target:
                l=i
                break
            else:
                if nums[-1] < target:
                    l = len(nums)
                    break
        return l

nums = [1,3,5,6]

target = 5

leetcode = Solution()

print(leetcode.searchInsert(nums,target))