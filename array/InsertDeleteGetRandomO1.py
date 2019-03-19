import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = {}
        self.idx = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.values:
            return False
        self.values[val] = len(self.idx)
        self.idx.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.values:
            return False
        delete_idx = self.values[val]
        last_val = self.idx[-1]
        self.values[val], self.values[last_val] = self.values[last_val], self.values[val]
        self.idx[delete_idx], self.idx[-1] = self.idx[-1], self.idx[delete_idx]
        self.values.pop(val)
        self.idx.pop()

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        random_idx = random.randint(0, len(self.idx) - 1)
        return self.idx[random_idx]


if __name__ == "__main__":
    s = RandomizedSet()
    s.insert(2)
    s.insert(3)
    s.insert(1)
    s.insert(4)
    s.remove(3)

    print(s.getRandom())
