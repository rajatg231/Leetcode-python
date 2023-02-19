// https://leetcode.com/problems/find-all-duplicates-in-an-array

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        set1= set()
        res=[]
        for num in nums:
            length1= len(set1)
            set1.add(num)
            if(length1==len(set1)):
                res.append(num)
                set1.remove(num)
        return res