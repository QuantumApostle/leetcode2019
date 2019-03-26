# LC 873
class Solution:
    def lenLongestFibSubseq(self, A):
        num_set = set(A)
        max_len = -1
        tmp_len = 2
        fib = [0, 0]
        tmp_set = set()
        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                fib[0] = A[i]
                fib[1] = A[j]
                tmp_sum = sum(fib)
                tmp_list = [fib[0], fib[1]]
                if (fib[0], fib[1]) in tmp_set:
                    continue
                while tmp_sum in num_set:
                    tmp_list.append(tmp_sum)
                    fib[0] = fib[1]
                    fib[1] = tmp_sum
                    tmp_sum = sum(fib)
                    tmp_len += 1
                    tmp_set.add((fib[0], fib[1]))
                max_len = max(tmp_len, max_len)
                tmp_len = 2
        return max_len if max_len != 2 else 0


if __name__ == "__main__":
    A = [2, 4, 7, 8, 9, 10, 14, 15, 18, 23, 32, 50]
    print(Solution().lenLongestFibSubseq(A))
