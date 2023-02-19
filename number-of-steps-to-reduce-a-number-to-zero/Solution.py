// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero

class Solution:
    def numberOfSteps(self, num: int) -> int:
        count=0
        while num!=0:
            count+=1
            if((num & 1)==0):
                num//=2
            else:
                num-=1
        return count