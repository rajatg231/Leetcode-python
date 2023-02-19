// https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        flag='pos'
        
        if(x==0):
            return 0
        if(x<0):
            flag='neg'
            x= -1*x
        ans=x%10
        x=x//10
        while(x>0):
            ans=ans*10
            ans+=x%10
            x=x//10
        if(ans>(2**31)-1) or (ans<((-2)**31)):
            return 0
        if(flag=='neg'):
            return ans*-1
        else:
            return ans
