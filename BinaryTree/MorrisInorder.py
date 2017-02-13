# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def morris(self, root):
        curt = root
        while curt:
            pre = curt.left
            if not pre:
                print(curt.val)
                curt = curt.right
            else:
                while pre.right and pre.right != curt:
                    pre = pre.right
                if not pre.right:
                    pre.right = curt
                    curt = curt.left
                else:
                    pre.right = None
                    print(curt.val)
                    curt = curt.right

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

print(Solution().morris(node1))

