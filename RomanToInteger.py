class solution:
    def romanToInteger(self,number:str,Dict:dict) -> int:
        sum = 0


        for n in range(0,len(number)):
            if (n < len(number) - 1 and  Dict[number[n]] >= Dict[number[n+1]] or n == len(number) - 1 ):
                sum = sum + Dict[number[n]]

            else:
                sum = sum - Dict[number[n]]

        return sum

Dict = dict({'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000})
number = 'MCMXCIV'
leetcode = solution()
returnval = leetcode.romanToInteger(number,Dict)
print(returnval)