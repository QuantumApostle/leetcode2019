import copy


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return []
        self.graph = {}
        if beginWord not in wordList:
            wordList.append(beginWord)
        for i in range(len(wordList) - 1):
            for j in range(i, len(wordList)):
                w1, w2 = wordList[i], wordList[j]
                # print(w1, w2)
                if self.connected(w1, w2):
                    self.graph.setdefault(w1, [])
                    self.graph[w1].append(w2)
                    self.graph.setdefault(w2, [])
                    self.graph[w2].append(w1)
        # print(self.graph)
        self.visited = set([beginWord])
        self.endWord = endWord
        self.result = []
        if not self.graph or not self.graph[beginWord]:
            return self.result
        self.dfs([beginWord])
        return self.result

    def dfs(self, cur_path):
        # print(cur_path)
        tail = cur_path[-1]
        if self.endWord in self.graph[tail]:
            cur_path.append(self.endWord)
            if not self.result or len(cur_path) == len(self.result[0]):
                self.result.append(copy.deepcopy(cur_path))
            cur_path.pop(-1)
        else:
            for w in self.graph[tail]:
                if w not in cur_path:
                    cur_path.append(w)
                    self.dfs(cur_path)
                    cur_path.pop(-1)

    def connected(self, w1, w2):
        count = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                count += 1
        return count == 1


if __name__ == "__main__":
    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot", "dog"]
    print(Solution().findLadders(beginWord, endWord, wordList))
