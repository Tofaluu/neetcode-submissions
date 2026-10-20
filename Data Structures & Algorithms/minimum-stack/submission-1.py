class MinStack:

    def __init__(self):
        self.arr = []
        self.length = 0
        self.minimum = []
        self.min_length = 0
    def push(self, val: int) -> None:
        self.arr.append(val)
        self.length += 1
        if not self.minimum or self.minimum[self.min_length - 1] >= val:
            self.minimum.append(val)
            self.min_length += 1
    def pop(self) -> None:
        if self.minimum[self.min_length - 1] == self.arr[self.length - 1]:
            self.minimum.pop()
            self.min_length -= 1
        self.arr.pop()
        self.length -= 1

    def top(self) -> int:
        return self.arr[self.length - 1]

    def getMin(self) -> int:
        return self.minimum[self.min_length - 1]