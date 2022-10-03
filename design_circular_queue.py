class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None]*k
        self.head = 0
        self.q_size = k
        self.end = 0
        self.count = 0
        
    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.queue[self.end] = value
            self.end = (self.end+1)%self.q_size
            self.count += 1
            return True

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.head = (self.head+1)%self.q_size
            self.count -= 1
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.end-1)%self.q_size]
        
    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.q_size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()