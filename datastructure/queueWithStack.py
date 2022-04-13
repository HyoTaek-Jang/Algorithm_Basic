class Queue:
    def __init__(self):
        self.add_stack = []
        self.pop_stack = []

    def add(self, value):
        self.add_stack.append(value)

    def pop(self):
        if len(self.pop_stack):
            value = self.pop_stack.pop()
            return value
        elif len(self.add_stack) == 0:
            raise Exception("큐가 비어있습니다.")

        while self.add_stack:
            self.pop_stack.append(self.add_stack.pop())

        return self.pop()


queue = Queue()
queue.add(5)
queue.add(1)
print(queue.pop())
queue.add(2)
queue.add(3)
print(queue.pop())
print(queue.pop())
print(queue.pop())
