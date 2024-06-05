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

class MinStack:

    def __init__(self):
        self._a = Stack()
        self._b = Stack()



    def push(self, val: int) -> None:
        if self._a.empty():
            self._a.push(val)
        elif val<=self._a.top():
            self._a.push(val)
        self._b.push(val)


    def pop(self) -> None:
        if self._a.top() == self._b.top():
            self._a.pop()
        self._b.pop()


    def top(self) -> int:
        return self._b.top()


    def getMin(self) -> int:
        return self._a.top()



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
