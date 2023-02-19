// https://leetcode.com/problems/separate-the-digits-in-an-array

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        for num in nums:
            if num<9:
                res.append(num)
            else:
                res1=[]
                while num>0:
                    res1.append(num%10)
                    num=num//10
                for i in range(len(res1)-1,-1,-1):
                    res.append(res1[i])
        return res
                    
                    
                    
                
        