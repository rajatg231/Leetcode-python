// https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict={}
        for c in s:
            if(dict.get(c,-1)==-1):
                dict[c]=1
            else:
                dict[c]+=1
        for c in t:
            if(dict.get(c,-1)==-1):
                return False
            else:
                dict[c]-=1
                if(dict[c]==0):
                    del dict[c]
        return not(bool(dict))
        