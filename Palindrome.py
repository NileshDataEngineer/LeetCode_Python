class Solution:
    def isPalindrome(self,num:int) -> bool:
        if str(num) == str(num)[::-1]:
            return True
        else:
            return False
num = 121
obj=Solution()
print(obj.isPalindrome(num))
