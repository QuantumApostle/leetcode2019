class Solution:
    def sumSubseqWidths(self, A):
        A.sort()
        k_mod = 1e9 + 7
        result = 0
        n = len(A)
        p = 1
        for i in range(n):
            result = (result + (A[i] - A[n - i - 1]) * p) % k_mod
            p = (int(p) << 1) % k_mod
        return int((result + k_mod) % k_mod)
