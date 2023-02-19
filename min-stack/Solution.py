// https://leetcode.com/problems/min-stack

class MinStack:

    def __init__(self):
        self.stack=[]
        

    def push(self, val: int) -> None:
        mins=val
        if(len(self.stack))>0:
            if(mins>self.stack[-1][1]):
                mins=self.stack[-1][1]
        self.stack.append([val,mins])

    def pop(self) -> None:
        if len(self.stack)>0:
            self.stack.pop()
            
        

    def top(self) -> int:
        if len(self.stack)>0:
            return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()