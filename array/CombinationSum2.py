from copy import deepcopy
class Solution:
    def combinationSum2(self, candidates, target):
        if not candidates:
            return []
        if len(candidates) == 1:
            return [] if candidates[0] != target else [[candidates[0]]]
        self.candidates = sorted(candidates)
        self.n = len(self.candidates)
        self.result = []
        self.target = target
        cur_idx = 0
        cur_sum = 0
        tmp_list = []
        self.dfs(cur_idx, tmp_list, cur_sum)
        return self.result

    def dfs(self, cur_idx, tmp_list, cur_sum):
        if cur_sum == self.target and tmp_list not in self.result:
            self.result.append(deepcopy(tmp_list))
        elif cur_sum < self.target:
            for i in range(cur_idx, self.n):
                if cur_sum + self.candidates[i] > self.target:
                    break
                cur_sum += self.candidates[i]
                tmp_list.append(self.candidates[i])
                self.dfs(i+1, tmp_list, cur_sum)
                tmp_list.pop()
                cur_sum -= self.candidates[i]


