# LC 108
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        def build_BST(start, end):
            if start > end:
                return None
            elif start == end:
                return TreeNode(nums[start])
            else:
                mid = int((start + end) / 2)
                root = TreeNode(nums[mid])
                root.right = build_BST(mid + 1, end)
                root.left = build_BST(start, mid - 1)
                return root

        return build_BST(0, len(nums) - 1)
