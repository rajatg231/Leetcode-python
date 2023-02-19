// https://leetcode.com/problems/power-of-three

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if(n<=0):
            return False
        elif(n==1):
            return True
        while(n>1):
            if(n%3!=0):
                return False
            else:
                n=n/3
        return True