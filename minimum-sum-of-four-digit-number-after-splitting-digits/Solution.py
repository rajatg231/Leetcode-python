// https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits

class Solution:
    def minimumSum(self, num: int) -> int:
        temp=[]
        while (num>0):
            temp.append(num%10)
            num=num//10
        temp1 = min(temp)*10+max(temp)
        temp.remove(max(temp))
        temp.remove(min(temp))
        temp2 = min(temp)*10 + max(temp)
        return temp1+temp2