# LC956
import copy, math


class Solution:
    def tallestBillboard(self, rods):
        s = sum(rods)
        dp = [0] + [-1] * s

        for h in rods:
            cur = copy.deepcopy(dp)
            for i in range(s - h+1):
                if cur[i] < 0:
                    continue
                dp[i + h] = max(dp[i + h], cur[i])
                diff = int(math.fabs(i - h))
                dp[diff] = max(dp[diff], cur[i] + min(h, i))

        return dp[0]
