__author__ = 'wfpeterson'
__project__ = 'testpython'


class Swap:
    def demo(self):
        a = int(input("a: "))
        b = int(input("b: "))
        a, b = self.swap(a, b)
        print(a, b)

    def swap(self, b):
        temp = b
        b = self
        self = temp
        return self, b

Swap().demo()