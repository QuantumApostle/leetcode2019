"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


from typing import List


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        cur_level = [root]
        next_level = []
        ans = []
        tmp = []
        import copy
        while cur_level:
            cur_node = cur_level.pop(0)
            if cur_node:
                tmp.append(cur_node.val)
                next_level += cur_node.children
            if not cur_level:
                if tmp:
                    ans.append(copy.deepcopy(tmp))
                    tmp = []
                    cur_level = next_level
                    next_level = []
        return ans
