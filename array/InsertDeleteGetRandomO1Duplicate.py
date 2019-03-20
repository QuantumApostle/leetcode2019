# LC 381
import random


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = {}
        self.idx = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        flag = False
        if val not in self.values:
            flag = True
            self.values.setdefault(val, [])

        self.values[val].append(len(self.idx))
        tmp = len(self.values[val])
        self.idx.append([val, tmp - 1])
        return flag

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.values or not self.values[val]:
            return False
        else:
            last_val = self.idx[-1][0]
            last_val_idx = self.idx[-1][1]

            delete_val_idx = self.values[val][-1]
            self.idx[-1], self.idx[delete_val_idx] = self.idx[delete_val_idx], self.idx[-1]
            self.values[last_val][last_val_idx], self.values[val][-1] = self.values[val][-1], self.values[last_val][last_val_idx]

            self.idx.pop()
            self.values[val].pop()
            if not self.values[val]:
                self.values.pop(val)
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self.idx[random.randint(0, len(self.idx) - 1)][0]


if __name__ == "__main__":
    s = RandomizedCollection()
    s.insert(1)
    s.insert(1)
    s.insert(2)
    s.insert(2)
    s.insert(2)
    s.remove(1)
    s.remove(1)
    s.remove(2)
    s.insert(1)
    s.remove(2)
