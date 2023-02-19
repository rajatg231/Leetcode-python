// https://leetcode.com/problems/partition-array-according-to-given-pivot

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small=[]
        large=[]
        equal=[]
        for num in nums:
            if num<pivot:
                small.append(num)
            elif num>pivot:
                large.append(num)
            else:
                equal.append(num)
        small.extend(equal)
        small.extend(large)
        return small
        # first=0
        # second=0
        # pivot_index=-1
        # while(first<len(nums)):
        #     while(nums[first]!=pivot):
        #         while(nums[first]<pivot):
        #             first+=1
        #         second=first
        #         while(nums[second]>pivot):
        #             second+=1
        #         nums[first], nums[second] = nums[second],nums[first]


          
        # return nums