# LC 896
class Solution:
    def isMonotonic(self, A):
        tmp = 0
        tmp1 = 0
        for i in range(len(A) - 1):
            j = i + 1
            if A[i] < A[j]:
                tmp += 1
            elif A[i] > A[j]:
                tmp -= 1
            else:
                tmp1 += 1
        return abs(tmp) + tmp1 == len(A) - 1
