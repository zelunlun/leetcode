# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        times = 0
        if root == None :
            return
        while root.left != None:
            if root.left: 
                self.maxDepth(root.left) 
                # root = root.left
            else:return 0
            if root.right: 
                self.maxDepth(root.right)
                # root = root.right
            else: return 0
            times += 1
        return times

tree = TreeNode(3,9,20)


ans = Solution()
ans.maxDepth(tree)