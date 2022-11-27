# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:        # 這一行的意思是什麼??
            return
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 


if __name__ == '__main__':
    tree = TreeNode(3,9,20)
    ans = Solution()
    ans.maxDepth(tree)



"""
    自己寫的 不知道在寫什麼碗糕
"""
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         left_times = 0
#         right_times = 0
#         if root == None :
#             return
#         while root.left or root.right :
#             if root.left == None:
#                 self.maxDepth(root.right)
#                 left_times += 1
#             elif root.right == None:
#                 self.maxDepth(root.left)
#                 right_times += 1
#         return max(left_times, right_times)
#         #     self.maxDepth(root.left) 
#         #     # root = root.left
#         # else:return 0
#         # if root.right: 
#         #     self.maxDepth(root.right)
#         #     # root = root.right
#         # else: return 0
#         times += 1
#         return times