class Solution:
    def is_valid(self, s):
        if s[0] == '0':
            return False
        else:
            return 1 <= int(s) <= 26

    def numDecodings(self, s):
        if not s or not self.is_valid(s[0]):
            return 0
        a = 1
        b = 1 if self.is_valid(s[0]) else 0
        c = 0
        if len(s) == 1:
            return b
        for i in range(2, len(s) + 1):
            c = 0
            if self.is_valid(s[i - 1:i]):
                c += b
            if self.is_valid(s[i - 2:i]):
                c += a
            a = b
            b = c
        return c
