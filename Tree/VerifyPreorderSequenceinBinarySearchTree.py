class Solution:
    def verifyPreorder(self, preorder):
        import sys
        low_bound = -sys.maxsize
        i = -1

        for n in preorder:
            if n < low_bound:
                return False
            while i >= 0 and n > preorder[i]:
                low_bound = preorder[i]
                i -= 1
            i += 1
            preorder[i] = n
            print(preorder)
        return True


preorder = [5, 2, 1, 3, 6]
assert Solution().verifyPreorder(preorder) == True
