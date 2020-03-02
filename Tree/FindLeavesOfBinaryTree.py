# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findLeaves(self, root: TreeNode):
        if not root:
            return []

        def find_leaves(root, current):
            if root:
                if not root.left and not root.right:
                    current.append(root.val)
                    return
                root.left = find_leaves(root.left, current)
                root.right = find_leaves(root.right, current)
                return root

        res = []
        while root:
            current = []
            root = find_leaves(root, current)
            res.append(current)
        return res


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
print(Solution().findLeaves(t1))
