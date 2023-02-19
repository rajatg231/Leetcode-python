// https://leetcode.com/problems/regular-expression-matching

import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        val=re.search(p,s)
        if val==None:
            return False
        if val.regs[0][0]==0 and val.regs[0][1]==len(s):
            return True
        else:
            return False