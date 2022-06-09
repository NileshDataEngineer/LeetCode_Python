from typing import List


class Solution:
    def longestCommonPrefix(self,strs:List[str]) -> str:
        prefix = ''
        for i in range(len(min(strs))):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix




strs = ["flower","flight","flow"]
leetcode=Solution()
x = leetcode.longestCommonPrefix(strs)
print(x)