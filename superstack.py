"""Implements a super stack"""


class SuperStack(object):

    def __init__(self):
        self.stack = list()

    def push(self, k: int) -> None:
        """Inserts entry to the list."""
        self.stack.append(k)

    def pop(self) -> int:
        """Pops the top element from the list"""
        return self.stack.pop()

    def inc(self, e: int, k: int) -> None:
        """Adds k to the bottom e elements of the stack."""
        if len(self.stack) < e:
            return

        for index in range(0, e):
            self.stack[index] += k
