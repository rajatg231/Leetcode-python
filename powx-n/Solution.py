// https://leetcode.com/problems/powx-n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return x**n
        res=1
        def cal(x,n):
            res=1
            while(n>=0):
                if n==0:
                    return 1
                if n%2!=0:
                    return x*cal(x,n-1)
                else:
                    x=x*x
                    n=n/2
                return cal(x,n)                
        if x==0:
            return 0
        if n==0:
            return res
        elif n>0:
            res=cal(x,n)
            return res
        else:
            n=n*-1
            res=cal(x,n)
            return 1/res
        
                