# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        while root.val != -1:
            res.append(self.remove_leaves(root))
            self.cut_leaves(root)
        return res

    def cut_leaves(self, root):
        if root:
            if root.left:
                if root.left.val == -1:
                    root.left = None
                else:
                    self.cut_leaves(root.left)
            if root.right:
                if root.right.val == -1:
                    root.right = None
                else:
                    self.cut_leaves(root.right)

    def remove_leaves(self, root):
        if root:
            tmp = []
            if not root.left and not root.right:
                tmp.append(root.val)
                root.val = -1
                return tmp
            else:
                tmp += self.remove_leaves(root.left)
                tmp += self.remove_leaves(root.right)
                return tmp


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
