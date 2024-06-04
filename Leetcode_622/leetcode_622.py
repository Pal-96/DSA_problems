class MyCircularQueue:

    def __init__(self, k: int):
        self._a = [-1]*k
        self._size = k
        self._front = 0
        self._rear = 0


    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self._a[self._rear%self._size] = value
            self._rear+=1
            return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self._front+=1
            return True


    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self._a[self._front%self._size]


    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self._a[(self._rear-1)%self._size]


    def isEmpty(self) -> bool:
        if self._front==self._rear:
            return True
        else:
            return False



    def isFull(self) -> bool:
        if self._rear - self._front == self._size:
            return True
        else:
            return False



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
