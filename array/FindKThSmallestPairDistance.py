class Solution:
    def smallestDistancePair(self, nums, k):
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        n = len(nums)

        while left < right:
            count, start = 0, 0
            mid = left + int((right - left) / 2)
            for i in range(len(nums)):
                while nums[i] - nums[start] > mid and start < n:
                    start += 1
                count += i - start
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == "__main__":
    nums = [9,10,7,10,6,1,5,4,9,8]
    k = 18
    print(Solution().smallestDistancePair(nums, k))
