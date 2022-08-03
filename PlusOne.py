class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = 0
        j = 1

        digits = digits[::-1]
        while j:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    j = 0
            else:
                digits.append(1)
                j = 0
            i += 1
        return digits[::-1]


digits = [1,2,3]

leetcode = Solution()

print(leetcode.plusOne(digits))