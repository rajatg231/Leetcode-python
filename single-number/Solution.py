// https://leetcode.com/problems/single-number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp=0
        for i in range(len(nums)):
            temp^=nums[i]
        return temp