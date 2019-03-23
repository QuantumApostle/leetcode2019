# LC 414
class Solution:
    def thirdMax(self, nums) -> int:
        tmp = []
        for i in range(len(nums)):
            if nums[i] in tmp:
                continue
            tmp.append(nums[i])
            tmp.sort()
            if len(tmp) > 3:
                tmp.pop(0)
        if len(tmp) < 3:
            return tmp[-1]
        return tmp[0]


if __name__ == "__main__":
    nums = [1, 2, 2, 5, 3, 5]
    print(Solution().thirdMax(nums))
