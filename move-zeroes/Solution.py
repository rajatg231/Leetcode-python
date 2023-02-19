// https://leetcode.com/problems/move-zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow=0
        fast=0
        while(slow<len(nums))and(fast<len(nums)):
            if nums[fast]==0:
                fast+=1
            elif nums[slow]==0 and slow<=fast:
                temp=nums[fast]
                nums[fast]=nums[slow]
                nums[slow]=temp
                slow+=1
            else:
                slow+=1
            if fast<slow and fast<len(nums):
                fast+=1