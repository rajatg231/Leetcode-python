// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        op=set(['(','{','['])
        # cl=set([')','}',']'])
        dict={'(':')', '{':'}','[':']'}
        stack=[]
        for b in s:
            if b in op:
                stack.append(b)
            else:
                if(len(stack)==0):
                    return False
                c=stack.pop()
                if dict[c]!=b:
                    return False
        if len(stack)==0:
            return True
        return False
