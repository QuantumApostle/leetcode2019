class Solution:

    def accountsMerge(self, accounts):
        self.merge_dict = {}
        self.reverse_merge_dict = {}
        self.emails_list = []
        self.union_find = {}
        for a in accounts:
            name = a[0]
            emails = a[1:]
            self.emails_list.append(emails)
            for e in emails:
                self.merge_dict[e] = name
                self.union_find[e] = e
                self.reverse_merge_dict.setdefault(name, set())
                self.reverse_merge_dict[name].add(e)
        for emails in self.emails_list:
            p = self.find_root(emails[0])
            self.union_find[emails[0]] = p
            if len(emails) > 1:
                for e in emails[1:]:
                    q = self.find_root(e)
                    self.union_find[e] = p
                    name = self.merge_dict[e]
                    for email in self.reverse_merge_dict[name]:
                        if self.union_find[email] == q:
                            self.union_find[email] = p
        result = []
        root = {}
        for e in self.union_find:
            p = self.union_find[e]
            root.setdefault(p, [])
            root[p].append(e)

        for e in root:
            result.append([self.merge_dict[e]] + sorted(root[e]))
        return result

    def find_root(self, e):
        p = self.union_find[e]
        if p != e:
            return self.union_find[p]
        else:
            return p

    # def accountsMerge1(self, accounts):
    #     self.merge_dict = {}
    #     for a in accounts:
    #         name = a[0]
    #         emails = a[1:]
    #         self.merge_dict.setdefault(name, [])
    #         self.merge_dict[name].append(set(emails))
    #     # print(self.merge_dict)
    #     result = []
    #     for name in self.merge_dict:
    #         tmp = []
    #         # print(self.merge_dict)
    #         while self.merge_dict[name]:
    #             tmp_set = self.merge_dict[name].pop()
    #             if not tmp:
    #                 tmp.append(tmp_set)
    #             else:
    #                 flag = False
    #                 for i in range(len(tmp)):
    #                     # print(tmp[i], tmp_set, tmp[i].intersection(tmp_set))
    #                     if len(tmp[i].intersection(tmp_set)) > 0:
    #                         tmp[i] = tmp[i].union(tmp_set)
    #                         # print(tmp[i], "@#$")
    #                         flag = True
    #                 if not flag:
    #                     tmp.append(tmp_set)
    #             # print(tmp)
    #         while tmp:
    #             tmp_set = tmp.pop()
    #             if not self.merge_dict[name]:
    #                 self.merge_dict[name].append(tmp_set)
    #             else:
    #                 flag = False
    #                 for i in range(len(self.merge_dict[name])):
    #
    #                     if len(self.merge_dict[name][i].intersection(tmp_set)) > 0:
    #                         self.merge_dict[name][i] = self.merge_dict[name][i].union(tmp_set)
    #                         # print(s, "!@#")
    #                         flag = True
    #                 if not flag:
    #                     self.merge_dict[name].append(tmp_set)
    #         for tmp_set in self.merge_dict[name]:
    #             result.append([name] + sorted(tmp_set))
    #
    #     return result


if __name__ == "__main__":
    accounts = [["Fern", "Fern8@m.co", "Fern9@m.co"], ["Fern", "Fern7@m.co", "Fern8@m.co"],
                ["Fern", "Fern4@m.co", "Fern5@m.co"], ["Fern", "Fern10@m.co", "Fern11@m.co"],
                ["Fern", "Fern9@m.co", "Fern10@m.co"], ["Fern", "Fern6@m.co", "Fern7@m.co"],
                ["Fern", "Fern1@m.co", "Fern2@m.co"], ["Fern", "Fern11@m.co", "Fern12@m.co"],
                ["Fern", "Fern3@m.co", "Fern4@m.co"], ["Fern", "Fern2@m.co", "Fern3@m.co"],
                ["Fern", "Fern5@m.co", "Fern6@m.co"], ["Fern", "Fern0@m.co", "Fern1@m.co"]]
    # print(Solution().accountsMerge(accounts))
    print(Solution().accountsMerge(accounts))
