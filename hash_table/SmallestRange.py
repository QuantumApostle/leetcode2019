from collections import Counter


class Solution:
    def smallestRange(self, nums):
        tmp_dict = {}
        for i, num_list in enumerate(nums):
            for n in num_list:
                tmp_dict.setdefault(n, set())
                tmp_dict[n].add(i)
        total_num_list = sorted(list(tmp_dict.keys()))

        n = len(total_num_list)
        i, j = 0, 0
        working_counter = Counter()
        working_counter.update(tmp_dict[total_num_list[0]])
        result = []

        while 0 <= i <= j < n:
            if len(working_counter) == len(nums):
                if not result:
                    result = [total_num_list[i], total_num_list[j]]
                elif total_num_list[j] - total_num_list[i] < result[1] - result[0]:
                    result = [total_num_list[i], total_num_list[j]]

                working_counter.subtract(tmp_dict[total_num_list[i]])
                counter_keys = list(working_counter.keys())
                for k in counter_keys:
                    if working_counter[k] == 0:
                        del working_counter[k]
                i += 1
            else:
                j += 1
                if j < n:
                    working_counter.update(tmp_dict[total_num_list[j]])

        return result


if __name__ == "__main__":
    nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    print(Solution().smallestRange(nums))
