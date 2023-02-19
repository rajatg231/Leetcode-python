// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        set1=set(banned)
        banned=list(set1)
        banned.sort()
        res=0
        sum=0
        temp=0
        for i in range(1,n+1):
            if temp<len(banned):
                j=temp
            else:
                j=len(banned)-1
            if banned[j]==i:
                j+=1
                temp=j
                continue
            while(j<len(banned)):
                if banned[j]<i:
                    j+=1
                    temp=j
                else:
                    break
            if sum+i<=maxSum:
                sum+=i
                res+=1
            elif sum+i>=maxSum:
                return res
        return res
                
                
        