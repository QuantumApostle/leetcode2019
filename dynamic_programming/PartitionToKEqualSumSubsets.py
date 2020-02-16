import copy


class Solution:
    #     def canPartitionKSubsets(self, nums, k):
    #         target = sum(nums) / k
    #         nums.sort()
    #         if max(nums) > target:
    #             return False
    #         length = len(nums)
    #         for i in range(length):
    #             if nums[-1] == target:
    #                 nums.pop(-1)
    #                 k -= 1
    #         bfs = [tuple([0 for x in range(k)])]
    #         for i in range(len(nums)):
    #             cur_len = len(bfs)
    #             print(cur_len)
    #             for l in range(cur_len):
    #                 cur_state = bfs.pop(0)
    #                 for j in range(k):
    #                     if cur_state[j] + nums[i] <= target:
    #                         tmp = copy.deepcopy(list(cur_state))
    #                         tmp[j] += nums[i]
    #                         bfs.append(tuple(tmp))
    #             bfs = list(set(bfs))
    #         return True if len(bfs) else False

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

        print(nums, k)
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


if __name__ == "__main__":
    nums = [4,3,2,3,5,2,1]
    k = 4
    print(Solution().canPartitionKSubsets(nums, k))
