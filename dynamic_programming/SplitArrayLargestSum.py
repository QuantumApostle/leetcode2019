# LC410
import sys


class Solution:
    def splitArray(self, nums, m):
        if not nums or len(nums) < m:
            return -1
        sum_list = self.get_sum_list(nums)
        dp = [[sys.maxsize / 2] * len(nums) for i in range(m)]
        # print(dp)
        dp[0] = sum_list
        for i in range(1, m):
            for j in range(i, len(nums)):
                for k in range(j):
                    dp[i][j] = min(dp[i][j], max(dp[i - 1][k], sum_list[j] - sum_list[k]))

        # self.print_table(dp)
        return dp[m - 1][len(nums) - 1]

    def get_sum_list(self, nums):
        result = []
        tmp = 0
        for i in range(len(nums)):
            tmp += nums[i]
            result.append(tmp)
        return result

    def print_table(self, a):
        for l in a:
            print(l)
        print("\n")


if __name__ == "__main__":
    m = 2
    nums = [7, 2, 5, 10, 8]
    # print(Solution().get_sum_list(nums))
    result = Solution().splitArray(nums, m)
    print(result)
