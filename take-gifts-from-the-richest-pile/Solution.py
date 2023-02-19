// https://leetcode.com/problems/take-gifts-from-the-richest-pile

import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # gifts.sort()
        temp=0
        for j in range(len(gifts)-1,len(gifts)-k-1,-1):
            temp=max(gifts)
            ind=gifts.index(temp)
            gifts[ind]=math.floor(math.sqrt(temp))
        res=0
        for num in gifts:
            res+=num
        return res
            
        