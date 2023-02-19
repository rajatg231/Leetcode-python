// https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def find(original, cloned, target):
            if(original):
                find(original.left, cloned.left, target)
                if(original.val==target.val):
                    self.ans= cloned
                find(original.right, cloned.right, target)
        find(original, cloned, target)
        return self.ans