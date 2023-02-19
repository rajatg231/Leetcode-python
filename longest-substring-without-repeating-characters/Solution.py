// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set1= set()
        res=0
        count=0
        for i in range(len(s)):
            j=i
            while(len(set1)==count and j<len(s)):
                set1.add(s[j])
                count+=1
                j+=1  
            j-=1              
            res=max(res,len(set1))
            count=0
            set1.clear()
            while(s[i]==s[j] and i!=j):
                i+=1           
        return max(res,len(set1))