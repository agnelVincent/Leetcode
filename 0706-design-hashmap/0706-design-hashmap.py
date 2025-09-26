class MyHashMap:

    def __init__(self):
        self.hash_table = []

    def put(self, key: int, value: int) -> None:
        for i in self.hash_table:
            if i[0] == key:
                i[1] = value
                return
        self.hash_table.append([key , value])

    def get(self, key: int) -> int:
        for i in self.hash_table:
            if i[0] == key:
                return i[1]
        return -1

    def remove(self, key: int) -> None:
        for i in range(len(self.hash_table)):
            if self.hash_table[i][0] == key:
                self.hash_table.pop(i)
                return
        return -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)