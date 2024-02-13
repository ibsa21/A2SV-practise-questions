class SnapshotArray:

    def __init__(self, length: int):
        
        self.stores = {index:[(0, 0)] for index in range(length)}
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.stores[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        
        pos = bisect_right(self.stores[index], (snap_id, float('inf')))
        # print(self.stores, index, pos)
        return self.stores[index][pos-1][1]
        # return 0
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# 11:34 PM