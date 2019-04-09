# LC 715

class RangeModule:

    def __init__(self):
        self.range_list = []

    def addRange(self, left: int, right: int) -> None:
        if left > right:
            return None
        input_range = [left, right]
        print("input interval is ", input_range)
        # self.range_list.append(input_range)
        left_end, right_end = 0, len(self.range_list) - 1

        if left >= self.range_list[0][0]:
            left_end = self.find(left)

        if right <= self.range_list[-1][1]:
            right_end = self.find(right)



        self.range_list.sort(key=lambda x: x[0])
        # print(self.range_list)
        self.merge_range()
        print(self.range_list)

    def merge_range(self):
        i = 0
        tmp = []
        while i < len(self.range_list):
            if tmp:
                r1 = tmp[-1][1]
                l2 = self.range_list[i][0]
                r2 = self.range_list[i][1]
                if r1 >= l2:
                    tmp[-1][1] = max(r1, r2)
                else:
                    tmp.append(self.range_list[i])
            else:
                tmp.append(self.range_list[i])
            i += 1
        self.range_list = tmp

    def queryRange(self, left: int, right: int) -> bool:
        print("query range: ", [left, right])
        if left > right or not self.range_list:
            return False
        # l, r = 0, len(self.range_list) - 1
        if left < self.range_list[0][0] or left > self.range_list[-1][1]:
            return False

        pos = self.find(left)
        return right <= self.range_list[pos][1]

    def removeRange(self, left: int, right: int) -> None:
        print("remove interval:", [left, right])
        if left > right or not self.range_list:
            return None
        if left > self.range_list[-1][1] or right < self.range_list[0][0]:
            return None

        left_end, right_end = 0, len(self.range_list) - 1

        if left >= self.range_list[0][0]:
            left_end = self.find(left)

        if right <= self.range_list[-1][1]:
            right_end = self.find(right)

        tmp = []
        if self.range_list[left_end][0] < left:
            tmp += self.range_list[:left_end]
            tmp.append([self.range_list[left_end][0], left])

        if self.range_list[right_end][1] > right:
            tmp.append([right, self.range_list[right_end][1]])
            tmp += self.range_list[right_end + 1:]
        self.range_list = tmp
        print(self.range_list)

    def find(self, val):
        l, r, m = 0, len(self.range_list) - 1, 0
        while l <= r:
            m = l + (r - l) // 2
            m_l = self.range_list[m][0]
            m_r = self.range_list[m][1]
            if m_l <= val <= m_r:
                break
            elif m_l < val:
                l = m + 1
            else:
                r = m
        return m


if __name__ == "__main__":
    s = RangeModule()
    s.queryRange(3, 6)
    s.addRange(3, 5)
    s.addRange(2, 4)
    s.addRange(6, 8)
    s.addRange(9, 12)
    # s.addRange(4, 10)

    # s.addRange(3, 7)
    print(s.queryRange(10, 12))

    s.removeRange(7, 13)
