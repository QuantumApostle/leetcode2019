class Solution:
    def canPartitionKSubsets(self, nums, k):
        target = sum(nums) / k
        nums.sort()
        if max(nums) > target:
            return False
        length = len(nums)
        for i in range(length):
            if nums[-1] == target:
                nums.pop(-1)
                k -= 1
        working_list = [0 for x in range(k)]
        self.result = False

        def dfs(idx=0):
            if idx == len(nums):
                self.result = True
            else:
                for j in range(k):
                    working_list[j] += nums[idx]
                    if working_list[j] <= target:
                        dfs(idx + 1)
                    working_list[j] -= nums[idx]

        dfs()
        return self.result
