class Solution:
    def findMissingRanges(self, nums, lower, upper):
        format_str = lambda a, b: '{}->{}'.format(str(a), str(b))
        if not nums:
            if lower < upper:
                return [format_str(lower, upper)]
            else:
                return [str(lower)]
        nums = [lower] + nums + [upper]
        result = []
        if nums[0] < nums[1]:
            if nums[1] - nums[0] == 1:
                result.append(str(nums[0]))
            else:
                result.append(format_str(nums[0], nums[1] - 1))
        i, j = 1, 2
        while i < len(nums) - 1 and j < len(nums) - 1:
            diff = nums[j] - nums[i] - 1
            if diff == 1:
                result.append(str(nums[i] + 1))
            elif diff > 1:
                result.append(
                    format_str(nums[i] + 1, nums[j] - 1)
                )
            i += 1
            j += 1
        if nums[-2] < nums[-1]:
            if nums[-1] - nums[-2] == 1:
                result.append(str(nums[-1]))
            else:
                result.append(format_str(nums[-2] + 1, nums[-1]))
        return result
