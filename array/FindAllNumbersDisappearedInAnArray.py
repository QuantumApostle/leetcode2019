# LC 448
class Solution:
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] = -1 * abs(nums[idx])
        result = []
        for j in range(len(nums)):
            if nums[j] > 0:
                result.append(j + 1)
        return result
