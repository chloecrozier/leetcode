# https://leetcode.com/problems/print-in-order/description/
class Foo:
    def __init__(self):
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()
        self.lock1.acquire()
        self.lock2.acquire()
        pass

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst() # printFirst() outputs "first". Do not change or remove this line.
        self.lock1.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.lock1:
            printSecond() # printSecond() outputs "second". Do not change or remove this line.
            self.lock2.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.lock1 and self.lock2:
            printThird() # printThird() outputs "third". Do not change or remove this line.
