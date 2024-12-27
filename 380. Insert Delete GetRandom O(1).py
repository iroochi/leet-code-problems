import random
class RandomizedSet:

    def __init__(self):
        self.value = []
        self.value_index = {}

    def insert(self, val: int) -> bool:
        if val in self.value_index:
            return False
        self.value_index[val] = len(self.value)
        self.value.append(val)
        return True
    def remove(self, val: int) -> bool:
        if val not in self.value_index:
            return False
        # finding the element
        index = self.value_index[val]
        last = self.value[-1]

        # swapping the last element 
        self.value[index] = last
        self.value_index[last] = index

        # removing the element
        self.value.pop()
        del self.value_index[val]
        return True


    def getRandom(self) -> int:
        return random.choice(self.value)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()