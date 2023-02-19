// https://leetcode.com/problems/find-the-array-concatenation-value

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        res=0
        def make(n1,n2):
            temp=[]
            concat=0
            while(n2>0):
                temp.append(n2%10)
                n2=n2//10
            concat=n1
            while len(temp)>0:
                concat=concat*10+temp.pop()
            return concat       
        while(l<=r):
            if l<r:
                res+=make(nums[l],nums[r])
            elif l==r:
                res+=nums[l]
            l+=1
            r-=1
        return res
            
            
        