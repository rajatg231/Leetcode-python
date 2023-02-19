// https://leetcode.com/problems/create-target-array-in-the-given-order

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            res.insert(index[i],nums[i])
        return res