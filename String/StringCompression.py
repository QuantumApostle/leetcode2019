# LC443

class Solution:
    def compress(self, chars):
        read_pointer, write_pointer = 0, 0
        while read_pointer < len(chars):
            chars[write_pointer] = chars[read_pointer]
            count = 1
            while read_pointer + 1 < len(chars) and chars[read_pointer] == chars[read_pointer + 1]:
                read_pointer += 1
                count += 1
            if count > 1:
                for c in str(count):
                    write_pointer += 1
                    chars[write_pointer] = c
            read_pointer += 1
            write_pointer += 1
        return write_pointer


if __name__ == "__main__":
    chars = [c for c in "aabbaa"]
    print(Solution().compress(chars))
