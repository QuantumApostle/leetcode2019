class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        password = []
        visited = set()
        def dfs(s: str):
            for x in map(str, range(k)):
                tmp_s = s + x
                if tmp_s not in visited:
                    visited.add(tmp_s)
                    dfs(tmp_s[1:])
                    password.append(x)
        dfs('0'*(n-1))
        return ''.join(password) + '0'*(n-1)