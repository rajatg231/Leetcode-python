// https://leetcode.com/problems/find-the-original-array-of-prefix-xor

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        if(len(pref)==1):
            return pref
        else:
            # res=[0]*len(pref)
            res=pref.copy()
            res[0]=pref[0]
            for i in range(1,len(pref)):
                res[i]=pref[i-1]^pref[i]
        return res
