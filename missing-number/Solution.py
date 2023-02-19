// https://leetcode.com/problems/missing-number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum=int((len(nums)*(len(nums)+1))/2)
        for num in nums:
            sum-=num
        return sum