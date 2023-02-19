// https://leetcode.com/problems/shuffle-string

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res=indices.copy()
        sep=""
        for i in range(len(indices)):
            res[indices[i]]=s[i]
        return sep.join(res)
