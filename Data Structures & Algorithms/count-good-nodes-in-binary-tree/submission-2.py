# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        res = 0

        def dfs(root,cmax):
            nonlocal res
            if not root: return

            if root.val >= cmax:
                res+=1
                cmax = root.val



            dfs(root.right,cmax)
            dfs(root.left,cmax)

            return


        dfs(root,float('-inf'))
        return res






        dfs(root, f)
        