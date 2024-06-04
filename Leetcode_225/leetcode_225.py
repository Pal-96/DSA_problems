class Queue:

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
    def __len__(self):
        return self._rear - self._front

class MyStack():

    def __init__(self, n:'size'=10):
        self._q = Queue(n)
        self._temp = Queue(n)


    def push(self, x: int) -> None:
        self._q.enQueue(x)

    def pop(self) -> int:
        while(len(self._q)!=1):
            self._temp.enQueue(self._q.Front())
            self._q.deQueue()
        removed = self._q.Front()
        self._q.deQueue()
        if self._q.isEmpty():
            [self._q,self._temp] = [self._temp, self._q]
        else:
            while(len(self._temp) == 0):
                self._q.enQueue(self._temp.deQueue())
        return removed


    def top(self) -> int:
        if self._q.isEmpty():
            return -1
        else:
            return self._q.Rear()


    def empty(self) -> bool:
        return self._q.isEmpty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
