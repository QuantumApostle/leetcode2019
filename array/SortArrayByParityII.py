# LC 922

class Solution:
    def sortArrayByParityII(self, A):
        i, j = 0, 1
        flag_i, flag_j = False, False
        while i < len(A) and j < len(A):
            if (i + A[i]) % 2 == 0:
                i += 2
            else:
                flag_i = True
            if (j + A[j]) % 2 == 0:
                j += 2
            else:
                flag_j = True
            if flag_i and flag_j:
                A[i], A[j] = A[j], A[i]
                i += 2
                j += 2
                flag_i, flag_j = False, False
        return A


if __name__ == "__main__":
    A = [648,831,560,986,192,424,997,829,897,843]
    print(Solution().sortArrayByParityII(A))
