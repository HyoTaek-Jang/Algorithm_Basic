class Queue:
    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def is_empty(self):
        return len(self.push_stack) + len(self.pop_stack) == 0

    def push(self, value):
        self.push_stack.append(value)

    def peek(self):
        if self.is_empty():
            raise Exception("큐가 비었음")
        self._move_stack()

        return self.pop_stack[-1]

    def pop(self):
        if self.is_empty():
            raise Exception("큐가 비었음")
        self._move_stack()

        return self.pop_stack.pop()

    def _move_stack(self):
        if len(self.pop_stack) == 0:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())


queue = Queue()
queue.push(1)
queue.push(3)
queue.push(6)
print(queue.peek())
queue.push(7)
print(queue.peek())
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())
queue.push(7)
print(queue.pop())
