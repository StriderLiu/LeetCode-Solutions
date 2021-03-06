# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        lSame, rSame = True, True
        lSame = self.isSameTree(p.left, q.left)
        rSame = self.isSameTree(p.right, q.right)
        if lSame and rSame and p.val == q.val:
            return True
        return False