// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range(len(nums)):
            if(dict.__contains__(nums[i])):
                dict[nums[i]]= (dict[nums[i]]+i)
            else:
                dict[nums[i]]=i
        for i in range(len(nums)):
            if(dict.__contains__(target-nums[i])):
                if((target-nums[i])!=(nums[i])):
                    return [i,dict.get(target-nums[i])]
                elif(i!=dict.get(target-nums[i])):
                    return [i,dict.get(target-nums[i])-i]