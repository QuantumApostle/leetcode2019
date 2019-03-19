# LC 763
class Solution:
    def partitionLabels(self, S):
        char_dict = {}
        for i in range(len(S)):
            char_dict[S[i]] = i

        result = []
        start = 0
        end = 0
        for j in range(len(S)):
            end = max(end, char_dict[S[j]])
            if j == end:
                result.append(end-start+1)
                start = end + 1
        return result

if __name__ == "__main__":
    S = "ababcbacadefegdehijhklij"
    print(Solution().partitionLabels(S))




