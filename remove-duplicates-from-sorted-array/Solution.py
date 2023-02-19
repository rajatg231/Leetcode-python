// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        org=0
        temp=nums[0]
        i=1
        while i<len(nums):
            if(nums[i]==temp):
                i+=1
            else:
                org+=1
                nums[org]=nums[i]
                temp=nums[org]
                i+=1
        return org+1

            