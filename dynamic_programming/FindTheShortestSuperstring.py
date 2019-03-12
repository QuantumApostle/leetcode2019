# LC943

class Solution:
    def shortestSuperstring(self, A):
        # build the dist table
        n = len(A)
        g = [[0] * n for i in range(n)]

        for i in range(n - 1):
            for j in range(i, n):
                if A[i] != A[j]:
                    g[i][j] = self.get_dist(A[i], A[j])
                    g[j][i] = self.get_dist(A[j], A[i])

        # build dp table
        import sys
        dp = [[sys.maxsize / 2] * n for i in range(1 << n)]
        # build parent table
        parent = [[-1] * n for i in range(1 << n)]
        # initialize
        for i in range(n):
            dp[1 << i][i] = len(A[i])

        # dp steps
        for state in range(1, 1 << n):
            for i in range(n):
                # if (state >> i) & 1 == 0:
                if state & (1 << i) == 0:
                    continue
                previous_state = state & ~(1 << i)
                for j in range(n):
                    if dp[state][i] > dp[previous_state][j] + g[j][i]:
                        dp[state][i] = dp[previous_state][j] + g[j][i]
                        parent[state][i] = j

        # reconstruct the state
        cur_str = -1
        tmp = sys.maxsize / 2
        for i in range(n):
            if dp[(1 << n) - 1][i] <= tmp:
                tmp = dp[(1 << n) - 1][i]
                cur_str = i
        cur_state = (1 << n) - 1
        result = A[cur_str]

        while cur_state >= 1:
            previous_str = parent[cur_state][cur_str]
            if previous_str < 0:
                break
            common_len = len(A[cur_str]) - g[previous_str][cur_str]
            tmp = A[previous_str][:len(A[previous_str]) - common_len]
            result = tmp + result
            cur_state = cur_state & ~(1 << cur_str)
            cur_str = previous_str

        return result

    def get_dist(self, s1, s2):
        tmp = [-1] * len(s1)
        for i in range(len(s1)):
            j = i
            k = 0
            while j < len(s1) and k < len(s2):
                if s1[j] == s2[k]:
                    tmp[j] = max(tmp[j], k)
                    j += 1
                    k += 1
                else:
                    break
        distance = len(s2) - 1 - tmp[-1]
        return distance

    def print_table(self, a):
        for l in a:
            print(l)
        print("\n")


if __name__ == "__main__":
    # A = ["catg", "ctaagt", "gcta", "ttca", "atgcatc"]
    # A = ["abcde", "xyzab"]
    # A = ["alex", "loves", "leetcode"]
    A = ["sssv", "svq", "dskss", "sksss"]
    print(A)
    # Solution().get_dist("dskss", "sssv")
    # Solution().get_dist("sksss", "sssv")
    result = Solution().shortestSuperstring(A)
    # print(result)
    # print("dsksssvq")
    assert (result == "dsksssvq")
