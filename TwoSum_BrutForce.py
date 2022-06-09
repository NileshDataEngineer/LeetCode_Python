from typing import List


class Solution:

    def twosum(self, lst: List[int], target: int) -> List[int]:

        listone = []
        for i in range(0, len(lst)):

            for j in range(i + 1, len(lst)):

                if lst[i] + lst[j] == target:
                    listone.append(i)
                    listone.append(j)
                    return listone


lst = [2, 5, 5, 11]

trg = 10
leetcode = Solution()
val = leetcode.twosum(lst, trg)
print(val)
