# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        closest = root.val
        # O(logN)
        while root:
            if abs(root.val - target) < abs(closest - target):
                closest = root.val
            root = root.left if target < root.val else root.right

        return closest