// https://leetcode.com/problems/single-number-iii

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        temp=0
        for num in nums:
            temp^=num
        #now temp contains XOR of only two elements which are not repeating
        #check which bit of temp is set
        check=temp
        count=0
        while(check):
            if(check&1)==1:
                break
            else:
                count+=1
            check=check>>1
        mask= 1<<count
        arr1=[]
        arr2=[]
        for num in nums:
            if mask& num==0:
                arr1.append(num)
            else:
                arr2.append(num)
        res1=0
        res2=0
        for num in arr1:
            res1^=num
        for num in arr2:
            res2^=num
        return [res1,res2]
