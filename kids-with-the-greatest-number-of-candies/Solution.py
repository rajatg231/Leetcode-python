// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res=[]
        maxCandy=max(candies)
        for i in range(len(candies)):
            if((candies[i]+extraCandies)>=maxCandy):
                res.append(True)
            else:
                res.append(False)
        return res