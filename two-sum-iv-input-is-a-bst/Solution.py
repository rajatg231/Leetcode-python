// https://leetcode.com/problems/two-sum-iv-input-is-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr=[]
        def inorder(root):
            if root==None:
                return
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        inorder(root)
        dict1={}
        for num in arr:
            if dict1.get(num,-1)==-1:
                dict1[num]=1
            else:
                dict1[num]+=1
        for num in arr:
            if num!=k-num and dict1.get(k-num,-1)!=-1:
                return True
        return False
