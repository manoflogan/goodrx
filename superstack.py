"""Implements a super stack"""


class SuperStack(object):

    def __init__(self):
        self.stack = list()

    def push(self, k: int) -> int:
        """Inserts entry to the stop of the stack."""
        self.stack.append(k)
        return k

    def pop(self) -> int:
        """Pops the top element from the list"""
        self.stack.pop()

    def inc(self, e: int, k: int) -> None:
        """Adds e to the bottom k elements of the stack."""
        if len(self.stack) < k:
            return

        for index in range(0, e):
            self.stack[index] += k
