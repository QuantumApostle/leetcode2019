# LC 654

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums) -> TreeNode:
        max_idx = -1
        max_value = -1
        if not nums:
            return None
        for i in range(len(nums)):
            if nums[i] > max_value:
                max_value = nums[i]
                max_idx = i
        root = TreeNode(max_value)
        root.left = self.constructMaximumBinaryTree(nums[:max_idx])
        root.right = self.constructMaximumBinaryTree(nums[max_idx + 1:])
        return root
