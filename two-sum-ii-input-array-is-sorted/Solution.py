// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while(i<j):
            tar=numbers[i]+numbers[j]
            if tar==target:
                break
            if tar>target:
                j-=1
            elif tar>target and numbers[j]<target:
                i+=1
                j-=1
            elif tar<target:
                i+=1
        return [i+1,j+1]
            

        # slow=0
        # fast=1
        # while slow<len(numbers) and fast<len(numbers):
        #     # fast=slow+1
        #     tar=numbers[slow]+numbers[fast]
        #     if tar<target and fast!=len(numbers)-1:
        #         fast+=1
        #     elif tar<target and fast==len(numbers)-1:
        #         slow+=1
        #         fast=slow+1
        #     elif tar>target:
        #         fast-=1
        #         slow+=1
        #     else:
        #         break
        # return [slow+1,fast+1]


