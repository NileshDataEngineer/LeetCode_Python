from typing import List




class Solution:

    def twosum(self, lst: List[int], target: int) -> List[int]:

        listone = []

        dic = {}
        for i,j in enumerate(lst):

            if target - j in dic:
                
                return [dic[target - j], i]
            else:
                dic[j] = i


lst = [2, 5, 5, 11]

trg = 10
leetcode = Solution()
print(leetcode.twosum(lst, trg))

# hello

