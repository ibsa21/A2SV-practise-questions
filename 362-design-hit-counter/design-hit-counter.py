class HitCounter:

    def __init__(self):
        self.arr = []

    def hit(self, timestamp: int) -> None:
        self.arr.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        return len(self.arr) - bisect_right(self.arr, timestamp - 300)

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)