// https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        op=set(['+','-','*','/'])
        for tok in tokens:
            if tok not in op:
                stack.append(int(tok))
            elif tok in op:
                v2=(stack.pop())
                v1=(stack.pop())
                if tok=='+':
                    stack.append(v2+v1)
                elif tok=='-':
                    stack.append(v1-v2)
                elif tok=='/':
                    stack.append(int(v1/v2))
                elif tok=='*':
                    stack.append(v2*v1)
        return stack.pop()





