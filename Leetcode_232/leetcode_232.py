class Stack():
    def __init__(self):
        # MUST USE ONLY PYTHON LIST
        self._a = []
        print("WRITE CODE")
        self._max_space = 0

    def push(self, T):
        self._a.append(T)
        if len(self._a) > self._max_space:
            self._max_space = len(self._a)

    def pop(self):
        if self.empty():
            return None
        else:
            return self._a.pop()

    def top(self):
        if self.empty():
            return None
        else:
            return self._a[len(self._a) - 1]

    def empty(self):
        if len(self._a):
            return False
        else:
            return True

    def space(self):
        return self._max_space

    def __len__(self):
        return len(self._a)


class MyQueue:

    def __init__(self):
        self._q = Stack()
        self._temp = Stack()


    def push(self, x: int) -> None:
        self._q.push(x)


    def pop(self) -> int:
        while(len(self._q)!=1):
            self._temp.push(self._q.pop())
        removed = self._q.top()
        self._q.pop()

        while(not self._temp.empty()):
            self._q.push(self._temp.pop())
        return removed


    def peek(self) -> int:
        while(len(self._q)!=1):
            self._temp.push(self._q.pop())
        peek = self._q.top()
        while(not self._temp.empty()):
            self._q.push(self._temp.pop())
        return peek

    def empty(self) -> bool:
        if len(self._q) == 0:
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
