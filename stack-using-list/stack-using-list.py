import sys
print(sys.version)

############################################################
# Stack.py
# Implements Stack object
###########################################################

###########################################################
#  class  Stack
# Our stack is infinite size
###########################################################
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


############################################################
# Util.py
###########################################################

############################################################
# NOTHING CAN BE CHANGED IN THIS FILE
###########################################################

############################################################
# All imports
###########################################################
import random
import math


class Util():
    pass

    ############################################
    # generate_random_number start to end INCLUDED
    # start to end INCLUDED
    #########################################
    def generate_a_random_number(self, start: int, end: int) -> 'int':
        v = random.randrange(start, end + 1)
        return v

    ############################################
    # generate_random_number GENERATES  N random numbers betweem
    # start to end INCLUDED
    # if onlypositive is False, generates both pos and negative number
    #  randrange(beg, end, step) :-
    #  beginning number (included in generation),
    #  last number (excluded in generation) a
    #  nd step ( to skip numbers in range while selecting).
    #########################################
    def generate_random_number(self, N: int, onlypositive: bool, start: int, end: int) -> 'List of integer':
        a = []
        for i in range(N):
            v = self.generate_a_random_number(start, end)
            if (onlypositive == False):
                if ((i % 2) == 0):  ##//Even. Half are positive, Half are negative
                    v = -v
            a.append(v)
        return a

    ############################################
    # swap
    #########################################
    def swap(self, a: 'List of integer', i: 'int', j: 'int'):
        t = a[i]
        a[i] = a[j]
        a[j] = t

    ############################################
    # generate shuffled number between 0 to n
    # n-1 not encluded
    #########################################
    def generate_suffled_number_between_1_to_n(self, n: int) -> 'List of integer':
        a = []
        for i in range(n):
            a.append(i)

        for i in range(n):
            j = self.generate_a_random_number(0, n - 1)
            k = self.generate_a_random_number(0, n - 1)
            self.swap(a, j, k)
        return a

    ############################################
    # generate shuffled number between 0 to n
    # n-1 not encluded
    #########################################
    def generate_duplicated_number_between_1_to_n(self, n: int) -> 'List of integer':
        a = []
        for i in range(n):
            a.append(i)

        for i in range(n):
            j = self.generate_a_random_number(0, n - 1)
            k = self.generate_a_random_number(0, n - 1)
            a[k] = a[j]
        return a

    ############################################
    # generate n numbers in ascending order from 0 to n-1
    #########################################
    def generate_n_numbers_in_ascending_order(self, n: int) -> 'List of integer':
        a = []
        for i in range(n):
            a.append(i)
        return a

    ############################################
    # generate n numbers in descending order from n-1 to 0
    #########################################
    def generate_n_numbers_in_descending_order(self, n: int) -> 'List of integer':
        a = []
        for i in range(n - 1, -1, -1):
            a.append(i)
        return a

    ############################################
    # generate n same k number
    #########################################
    def generate_n_same_k_number(self, n: int, k: 'int') -> 'List of integer':
        a = []
        for i in range(n):
            a.append(k)
        return a

    ############################################
    # print_index(10)
    #    0   1   2   3   4   5   6   7   8   9
    #########################################
    def print_index(self, n: int):
        for i in range(n):
            print("{:4d}".format(i), end="")
        print()

    ############################################
    # a = [7,8,9, 23, 100]
    # print_list(a)
    # 7   8   9  23 100
    #########################################
    def print_list(self, a: 'list'):
        for i in range(len(a)):
            print("{:4d}".format(a[i]), end="")
        print()

    ############################################
    # a = [7,8,9, 1, 100]
    # crash
    #########################################
    def assert_ascending_range(self, a: 'list', start: int, includingend: int):
        t = a[start]
        for i in range(start + 1, includingend):
            if (a[i] < t):
                assert (False)
            t = a[i]

    ############################################
    # a = [7,8,9, 1, 100]
    # crash
    #########################################
    def assert_ascending(self, a: 'list'):
        if (len(a)):
            self.assert_ascending_range(a, 0, len(a))

            ############################################

    # a = [1,2,3, 3, 4]
    # return True
    #########################################
    def is_ascending_order_has_duplicates(self, a: 'list') -> 'bool':
        if (len(a)):
            t = a[0]
            for i in range(1, len(a)):
                if (a[i] <= t):
                    return True
                t = a[i]
        return False

    ############################################
    # log to the next possible integer
    #########################################
    def log_upper_bound(self, n: 'int', b: 'int') -> 'int':
        f = math.log(n, b)
        c = math.ceil(f)
        return c

        ############################################

    # log to the smallest possible integer
    #########################################
    def log_lower_bound(self, n: 'int', b: 'int') -> 'int':
        f = math.log(n, b)
        c = math.floor(f)
        return c

        ############################################

    # sqrt to the next possible integer
    #########################################
    def sqrt_upper_bound(self, n: 'int') -> 'int':
        f = math.sqrt(n)
        c = math.ceil(f)
        return c

        ############################################

    # sqrt to the smallest possible integer
    #########################################
    def sqrt_lower_bound(self, n: 'int') -> 'int':
        f = math.sqrt(n)
        c = math.floor(f)
        return c

        ############################################

    # TEST DRIVERS BELOW
    #########################################
    def _test_random(self, N: int, onlypositive: bool, start: int, end: int) -> 'None':
        a = self.generate_random_number(N, onlypositive, start, end)
        assert (len(a) == N)
        self.print_index(N)
        self.print_list(a)

############################################################
# SQTest.py
# Test Bench for Stack
###########################################################

############################################################
#  NOTHING CAN BE CHANGED IN THIS FILE
###########################################################

############################################################
#  All imports here
###########################################################
import sys  # For getting Python Version

'''
from Util import *
from Stack import *
'''


############################################################
#  class  SQTest test
###########################################################
class SQTest():
    def __init__(self):
        self._u = Util()
        self._show = True

    ############################################################
    # test stack
    ###########################################################
    def _test_stack(self, W: 'string', N: 'int', K: 'int', show: 'bool'):
        print("Testing on", N, "elements started", W)
        if W == "using_python_list_of_unknown_size":
            s = Stack()
        else:
            assert (False)

        for i in range(N):
            s.push(i)

        for i in range(K):
            if (show):
                print(s.top(), " ", end='')
            s.pop()
        if (show):
            print()

        l = len(s)
        if (l != (N - K)):
            print("The stack must have", N - K, "element now. But you have ", l, "elements")
            assert (False)

        e = s.empty()
        if (N == K):
            if (e == False):
                print("The stack must be empty. But you are NOT 1")
                assert (False)
        else:
            assert (e == False)

        if (W == "using_python_list_of_unknown_size"):
            s = Stack()
        else:
            assert (False)
        for i in range(N):
            s.push(i)
            s.pop()
            if (W == "using_python_list_of_unknown_size"):
                l = s.space()
                if (l != 1):
                    print("You are taking", l, " spaces. Why?")
                    assert (False)
            elif (W == "using_queue"):
                l = len(s)
                if (l != 0):
                    print("Why you have ", l, "elements?")
                    assert (False)
            else:
                assert (False)

        e = s.empty()
        if (e == False):
            print("The stack must be empty. But you are NOT 2")
            assert (False)

        print("Testing on", N, "elements Passed")


############################################################
# Test stack
###########################################################
def test_stack(W: 'data_structure_used'):
    print("Testing stack ", W)
    s = SQTest()
    N = 5
    show = True
    s._test_stack(W, N, N - 1, show)

    N = 5
    show = True
    s._test_stack(W, N, N, show)

    N = 100
    show = True
    s._test_stack(W, N, N - 57, show)

    if (W == "using_python_list_of_unknown_size"):
        N = 500000
        show = False
        s._test_stack(W, N, N - 8602, show)

        N = 500001
        show = False
        s._test_stack(W, N, N, show)
        print("All the above function must have O(1) time and O(1) space for A grade")


############################################################
# main
###########################################################
def main():
    print(sys.version)
    test_stack("using_python_list_of_unknown_size")
    print("All my test passed")


############################################################
# start up
###########################################################
if (__name__ == '__main__'):
    main()
