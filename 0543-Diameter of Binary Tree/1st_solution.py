# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    # def insert(self, value):
    #     if self.val:
    #         if self.left:
    #             self.insert()
    #         elif self.left and self.right:
                
    #         else:
    #             self.left = TreeNode(value)
    #     else:
    #         self.val = value 
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        height = 0
        if root == None:
            return
        if root.left:
            height += 1
            self.diameterOfBinaryTree(root.left)
        return height


if __name__ == '__main__':
    ans = Solution()
    datas = [1,2,3,4,5]
    # for data in datas:
