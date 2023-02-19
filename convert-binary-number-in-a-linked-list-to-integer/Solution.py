// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        current=head
        res=[]
        num=0
        while(current!=None):
            res.append(current.val)
            current = current.next
        for i in range(len(res)):
            num+= res[i]*(2**(len(res)-1-i))
        return num
