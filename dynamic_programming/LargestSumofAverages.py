# LC813

class Solution:
    def largestSumOfAverages(self, A, K):
        dp = [[0 for x in range(len(A))] for y in range(K)]
        for i in range(len(A)):
            dp[0][i] = sum(A[:i + 1]) / float(i + 1)
        p = [0]
        for x in A: p.append(p[-1] + x)

        def average(i, j):
            if i == j:
                return A[i]
            return float(p[j + 1] - p[i]) / (j - i + 1)

        for k in range(1, K):
            for i in range(k, len(A)):
                for j in range(i):
                    dp[k][i] = max(dp[k - 1][j] + average(j + 1, i), dp[k][i])
        return dp[K - 1][-1]


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6, 7]
    # A = [9, 1, 2, 3, 9]
    K = 4
    # K = 3
    print(Solution().largestSumOfAverages(A, K))
