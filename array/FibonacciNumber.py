# LC 509
class Solution:
    def fib(self, N: int) -> int:
        f = [0, 1]
        if N in f: return N
        tmp = 0
        for i in range(2, N+1):
            tmp = f[0] + f[1]
            f[0] = f[1]
            f[1] = tmp
        return tmp


if __name__ == "__main__":
    print(Solution().fib(10))
