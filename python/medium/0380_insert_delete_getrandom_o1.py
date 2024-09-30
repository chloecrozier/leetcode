# https://leetcode.com/problems/insert-delete-getrandom-o1/description/
class RandomizedSet:

    def __init__(self):
        self.valSet = []
        self.valMap = {}

    def insert(self, val: int) -> bool:
        if val in self.valMap:
            return False
        else:
            self.valSet.append(val)
            self.valMap[val] = len(self.valSet) - 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.valMap:
            index = self.valMap[val]

            lastKey = self.valSet[-1]
            self.valSet[index] = lastKey
            self.valMap[lastKey] = index

            self.valSet.pop()
            self.valMap.pop(val)
            return True
        else:
            return False


    def getRandom(self) -> int:
        return random.choice(self.valSet)
