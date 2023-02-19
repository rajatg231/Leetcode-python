// https://leetcode.com/problems/sort-colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dict={}
        for num in nums:
            if dict.get(num,-1)==-1:
                dict[num]=1
            else:
                dict[num]+=1
        num=0
        i=0
        while num<3:
            while (dict.get(num,-1)!= -1) and (dict[num])>0:
                nums[i]=num
                i+=1
                dict[num]-=1
            num+=1