class Solution:
    def isValid(self,string:str) -> bool:
        Dict ={')':'(','}':'{',']':'['}
        stack =[]
        if len(string) == 0:
            return False
        for i in string:
            if i in Dict.values():
                stack.append(i)
            elif stack and Dict[i] == stack[-1]:
                stack.pop()
            else:
                return False
        return  stack == []
s = '()'
leetcode = Solution()
print(leetcode.isValid(s))


