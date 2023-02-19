// https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=[]
        for i in strs[0]:
            res.append(i)
        for word in strs:
            i=0
            count=0
            while((i<len(res))and(i<(len(word)))and(word[i]==res[i])):
                i+=1
                count+=1
            for j in range(count,len(res)):
                del res[count]
        temp=""
        return temp.join(res)
            