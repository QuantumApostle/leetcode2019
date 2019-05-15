class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = total_sum = 0
        n = len(nums)
        tmp = {0: 1}
        for i in range(n):
            total_sum += nums[i]
            tmp.setdefault(total_sum - k, 0)
            res += tmp[total_sum - k]
            tmp.setdefault(total_sum, 0)
            tmp[total_sum] += 1
        return res
