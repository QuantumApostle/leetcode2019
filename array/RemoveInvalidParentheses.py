class Solution:
    def removeInvalidParentheses(self, s: str) -> list:
        if not s:
            return ['']
        if len(s) == 1 and s in '()':
            return ['']

        def is_valid(s):
            tmp = []
            for c in s:
                if c == '(':
                    tmp.append('(')
                elif c == ')':
                    if tmp:
                        tmp.pop()
                    else:
                        return False
            return not tmp

        def dfs(s):
            if s:
                if is_valid(s):
                    if len(s) > self.max_len:
                        self.result = [s]
                        self.max_len = len(s)
                    elif len(s) == self.max_len:
                        self.result.append(s)
                else:
                    for i in range(len(s)):
                        if s[i] in '()':
                            tmp = s[:i] + s[i + 1:]
                            dfs(tmp)

        self.max_len = 0
        self.result = []
        dfs(s)
        if not self.result:
            return ['']
        else:
            return list(set(self.result))


test = ")("
print(Solution().removeInvalidParentheses(test))
