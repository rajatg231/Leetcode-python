// https://leetcode.com/problems/running-sum-of-1d-array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res=nums
        for i in range(1,len(nums)):
            res[i]=nums[i]+res[i-1]
        return res
